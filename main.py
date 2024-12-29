import logging

from pipebot import PipeBot
from pipebot.utils import compute_saliency, find_largest_contour

from pins import *


logging.basicConfig(level=logging.INFO, format="[{asctime}][{levelname:>9}][{name}] {message}", style="{")


def main() -> None:
    superbot = PipeBot()
    
    logging.info("Setting face, tyre, pump pins and initializing camera")
    superbot.set_face_pins(STEPPER_IN1, STEPPER_IN2, STEPPER_IN3, STEPPER_IN4)
    superbot.set_tyre_pins(TYERS_IN1, TYRES_IN2)
    superbot.set_pump_pins(PUMP_IN1, PUMP_IN2)

    superbot.init_camera()

    face_rotation = 0
    distance_travelled = 0
    detected_anomalies = 0

    while distance_travelled < 1.2:
        logging.info("Moving forward")
        superbot.move_robot(0.5, "forward")
        
        for _ in range(10):
            logging.info("Capturing image")
            image = superbot.capture_image()

            logging.info("Computing saliency mask")
            mask = compute_saliency(image)

            logging.info("Finding possible anomaly contour")
            contour = find_largest_contour(mask)

            if contour:
                detected_anomalies += 1

                logging.info("Found anomaly, rotating face 180deg for spray")
                superbot.rotate_face(256, "anti-clockwise")

                logging.info("Spraying chemical")
                superbot.run_pump(5)

                logging.info("Returning face to anomaly and continuing")
                superbot.rotate_face(256, "clockwise")
                superbot.rotate_face(51, "clockwise")
                face_rotation -= 51
                
            else:
                logging.info("No anomaly found, rotating face")
                superbot.rotate_face(51, "clockwise")
                face_rotation -= 51
        
        logging.info("Returning face to origin")
        superbot.rotate_face(abs(face_rotation), "anti-clockwise")
        face_rotation = 0

        distance_travelled += 0.2
        

if __name__ == "__main__":
    main()
