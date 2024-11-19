#LED
LED = 23 # Broadcom pin 23 (P5 pin 16)

# Tyres Controller
TYERS_IN1 = 17    #pin 17 (P5 pin 11) 3 motors drive
TYRES_IN2 = 27    #pin 27 (P5 pin 13) 
MOTOR2_IN3 = 22    #pin 22 (P5 pin 15)
MOTOR2_IN4 = 26    #pin 26 (P5 pin 13) pump

# Pump Controller
PUMP = 25    #pin 25 (P5 pin 22)

# Stepper Motor
STEPPER_IN1 = 21    #pin 21 (P5 pin 40)
STEPPER_IN2 = 20    #pin 20 (P5 pin 38)
STEPPER_IN3 = 15    #pin 15 (P5 pin 10)
STEPPER_IN4 = 14    #pin 14 (P5 pin 8)

# I2C Pin Setup:
# GPIO2 -> SDA (Data line for I2C)
# GPIO3 -> SCL (Clock line for I2C)
# These pins are automatically used when you enable I2C in raspi-config.

# Ultrasonic Sensor
ULTRASONIC_TRIG = 4    # Pin 4 (P5 pin 7)
ULTRASONIC_ECHO = 5    # Pin 5 (P5 pin 29)
