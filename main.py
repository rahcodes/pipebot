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
ledPin = 23 # Broadcom pin 23 (P1 pin 16)
