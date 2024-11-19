from pipebot import PipeBot
from time import sleep


def main() -> None:
    eagle = PipeBot()

    # eagle.set_diameter_reader_pin(echo=24, trig=23)
    # eagle.get_diameter()

    # eagle.set_face_pins(in_1=14, in_2=15, in_3=18, in_4=23)
    # eagle.rotate_face(steps=512, direction="clockwise")

    # eagle.init_accelerometer()
    # print(eagle.get_acceleration())
    # print(eagle.get_pitch_roll())

    # eagle.set_flashlight_pin(4)
    # eagle.switch_flashlight(state=1)

    # eagle.set_tyre_pins(in_1=17, in_2=27, in_3=15, in_4=18)
    # eagle.move_robot(duration=2, direction="forward")


if __name__ == "__main__":
    main()

# Pin Definitons:
ledPin = 23 # Broadcom pin 23 (P5 pin 16)

# GPIO pin configuration
# Motor Controller 1
MOTOR1_IN1 = 17    #pin 17 (P5 pin 11)
MOTOR1_IN2 = 27    #pin 27 (P5 pin 13)
MOTOR1_EN = 12  # PWM0_CHAN0 ; pin 12 (P5 pin 32)

MOTOR2_IN3 = 22    #pin 22 (P5 pin 15)
MOTOR2_IN4 = 26    #pin 26 (P5 pin 13)
MOTOR2_EN = 13  # PWM0_CHAN1 ; pin 13 (P5 pin 33)

# Motor Controller 2
MOTOR3_IN1 = 25    #pin 25 (P5 pin 22)
MOTOR3_IN2 = 5     #pin 5 (P5 pin 29)
MOTOR3_EN = 18  # PWM0_CHAN2 ; pin 12 (P5 pin 29)

MOTOR4_IN3 = 16    #pin 16 (P5 pin 36)
MOTOR4_IN4 = 6     #pin 6 (P5 pin 31)
MOTOR4_EN = 19  # PWM0_CHAN3 ; pin 19 (P5 pin 35)
