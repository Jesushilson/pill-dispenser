#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# Motor 1 via GPIO
m1_in1 = 5
m1_in2 = 6
m1_in3 = 12
m1_in4 = 13

# Motor 2 via GPIO
m2_in1 = 22
m2_in2 = 23
m2_in3 = 24
m2_in4 = 25

# Universal variables for the GPIO motors
step_sleep = 0.002
step_count = 4096
step_sequence = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

# Step Counter for both motors 
motor1_step_counter = 0
motor2_step_counter = 0

# Steps the motor 
def step_motor(steps, motorType, motor_step_counter, direction=True):
    if motorType == "motor_1":
        motor_pins = [m1_in1, m1_in2, m1_in3, m1_in4]
    else:
        motor_pins = [m2_in1, m2_in2, m2_in3, m2_in4]

    
    GPIO.setmode(GPIO.BCM)

    for pin in motor_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    try:
        for _ in range(steps):
            for pin in range(4):
                GPIO.output(
                    motor_pins[pin],
                    step_sequence[motor_step_counter][pin]
                )

            if direction:
                motor_step_counter = (motor_step_counter + 1) % 8
            else:
                motor_step_counter = (motor_step_counter - 1) % 8

            time.sleep(step_sleep)

    finally:
        for pin in motor_pins:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

def moveToContainer():
    step_motor(800, "motor_1", motor1_step_counter)

def moveToSize(size):
    step_motor(800, "motor_2", motor2_step_counter, False)

if __name__ == "__main__":
    moveToContainer()