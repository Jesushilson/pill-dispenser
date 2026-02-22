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

# Universal Distance Between Containers
STEPS_BETWEEN = 2400

# what the program thinks the 1st mechanism is at
current_container = 1 

# what the program thinks the 2nd mechanism is at
current_size = 1

size_dict = {
    1 : "large",
    2 : "medium",
    3: "small", 
    4: "long",
    5: "short"
}




# Steps the motor 
def step_motor(steps, motorType, direction=True):
    if motorType == "motor_1":
        motor_pins = [m1_in1, m1_in2, m1_in3, m1_in4]
    else:
        motor_pins = [m2_in1, m2_in2, m2_in3, m2_in4]
    motor_step_counter = 0
    
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

def moveToContainer(target_container):
    global current_container

    diff = current_container - target_container
    if diff == 0:
        return
    steps = abs(diff) * STEPS_BETWEEN
     
    # Go the direction where the desination is the closest
    direction = True if diff > 0 else False 

    step_motor(steps, "motor 1", direction)
    current_container = target_container

def moveToSize(target_size):
    global current_size

    diff = current_size - target_size
    if diff == 0:
        return
    steps = abs(diff) * STEPS_BETWEEN

    direction = True if diff > 0 else False 

    step_motor(steps, "motor 2", direction)
    current_size = target_size

def restart_mechanisms():
    moveToContainer(1)
    moveToSize(1)


if __name__ == "__main__":
    moveToContainer()