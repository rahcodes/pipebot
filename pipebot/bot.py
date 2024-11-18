import math

from gpiozero import LED, DistanceSensor, OutputDevice
from time import sleep
from board import I2C
from subprocess import check_output
from adafruit_adxl34x import ADXL345
from typing import Literal

from .constants import STEPPER_SIGNALS, ACCELEROMETER_ADDRESS


class PipeBot:
    def __init__(self) -> None:
        self._camera: None = None
        self._flashlight: LED | None = None
        self._diameter_reader: DistanceSensor | None = None
        self._face_pins: list[OutputDevice] | None = None
        self._accelerometer: ADXL345 | None = None
        self._tyre_pins: list[OutputDevice] | None = None
        self._pump: OutputDevice | None = None

    def init_camera(self) -> None:
        """Initializes camera"""

        raise NotImplemented("init_camera method is not implemented yet.")

    def capture_image(self) -> None:
        """Captures and returns the image from the camera"""

        assert self._camera, "Camera is not initialized."
        raise NotImplemented("capture_image method is not implemented yet.")

    def set_flashlight_pin(self, pin: int) -> None:
        """Sets the pin for LEDs used for the camera"""

        self._flashlight = LED(pin)
        self._flashlight.on()

    def switch_flashlight(self, state: Literal[0, 1]) -> None:
        """Switches on/off the camera flashlight. States: 0 for Off, 1 for On"""

        assert self._flashlight, "Flashlight pin is not set."
        assert state in [0, 1], f"Invalid state for flashlight '{state}'"

        if state == 0:
            self._flashlight.on()
        elif state == 1:
            self._flashlight.off()

    def set_diameter_reader_pins(self, echo: int, trig: int) -> None:
        """Sets the ultrasonic sensor pins (echo, trig) for the diameter reader"""

        self._diameter_reader = DistanceSensor(echo, trig)

    def get_diameter(self) -> float:
        """Returns the diameter of the pipe in centimeters(cm)"""

        assert self._diameter_reader, "Diameter reader pins are not set."

        return self._diameter_reader.distance * 100 * 2

    def set_face_pins(self, in_1: int, in_2: int, in_3: int, in_4: int) -> None:
        """Sets the pins for the stepper motor of the face (IN1, IN2, IN3, IN4)"""

        self._face_pins = [OutputDevice(pin) for pin in (in_1, in_2, in_3, in_4)]

    def rotate_face(
        self,
        steps: int,
        direction: Literal["clockwise", "anti-clockwise"],
        step_delay: float = 0.001,
    ) -> None:
        """Rotates the face in the given direction and number of steps (512 = 360deg)"""

        assert self._face_pins, "Face pins are not set."
        assert direction in [
            "clockwise",
            "anti-clockwise",
        ], "Direction must be clockwise or anti-clockwise."

        signals = (
            STEPPER_SIGNALS
            if direction == "anti-clockwise"
            else list(map(lambda sig: sig[::-1], STEPPER_SIGNALS))
        )

        for _ in range(steps):
            for halfstep in range(8):
                for pin in range(4):
                    if signals[halfstep][pin] == 1:
                        self._face_pins[pin].on()
                    else:
                        self._face_pins[pin].off()
                sleep(step_delay)

    def init_accelerometer(self) -> None:
        """Initializes I2C for accelerometer. Connection must be SDA->GPIO2 and SCL->GPIO3"""

        output = check_output(["i2cdetect", "-y", "1"])
        hex_address = f"{ACCELEROMETER_ADDRESS:02X}"

        if hex_address in output.decode():
            self._accelerometer = ADXL345(I2C())
        else:
            raise Exception(
                "Accelerometer not found. Check connection: SDA->GPIO2 and SCL->GPIO3"
            )

    def get_acceleration(self) -> tuple[float, float, float]:
        """Returns (x, y, z) acceleration in m/s^2"""

        assert self._accelerometer, "Accelerometer is not initialized."

        return self._accelerometer.acceleration

    def get_pitch_roll(self) -> tuple[float, float]:
        """Returns (pitch, roll) in degrees"""

        assert self._accelerometer, "Accelerometer is not initialized."

        x, y, z = self._accelerometer.acceleration

        pitch = math.atan2(x, math.sqrt(y**2 + z**2)) * (180.0 / math.pi)
        roll = math.atan2(y, math.sqrt(x**2 + z**2)) * (180.0 / math.pi)

        if z < 0:
            roll = 180.0 - abs(roll)

        return (pitch, roll)

    def set_tyre_pins(self, in_1: int, in_2: int, in_3: int, in_4: int) -> None:
        """Sets the pins for motor controller of the tyres (IN1, IN2, IN3, IN4)"""

        self._tyre_pins = [OutputDevice(pin) for pin in (in_1, in_2, in_3, in_4)]

    def move_robot(
        self, duration: float, direction: Literal["forward", "backward"]
    ) -> None:
        """Moves the robot forward/backward for given duration (seconds) and direction"""

        assert self._tyre_pins, "Tyre pins are not set."
        assert direction in [
            "forward",
            "backward",
        ], f"Invalid direction to move '{direction}'"

        if direction == "forward":
            self._tyre_pins[0].on()
            self._tyre_pins[2].on()
        else:
            self._tyre_pins[1].on()
            self._tyre_pins[3].on()

        sleep(duration)
        [pin.off() for pin in self._tyre_pins]

    def set_pump_pin(self, pin: int) -> None:
        """Sets the pin for the pump motor"""

        self._pump = OutputDevice(pin)

    def run_pump(self, duration: float) -> None:
        """Runs the pump for given duration in seconds"""

        assert self._pump, "Pump pin is not set."

        self._pump.on()
        sleep(duration)
        self._pump.off()
