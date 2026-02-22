#!/usr/bin/python3

import RPI.GPIO as GPIO # type: ignore
import time

m1_in1 = 5
m1_in2 = 6
m1_in3 = 12
m1_in4 = 13

m2_in1 = 22
m2_in2 = 23
m2_in3 = 24
m2_in4 = 25

step_sleep = 0.002

step_count = 4096

step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]


def moveToContainer():
    
    direction = False # counter clockwise
    GPIO.setmode( GPIO.BCM )
    GPIO.setup( m1_in1, GPIO.OUT )
    GPIO.setup( m1_in2, GPIO.OUT )
    GPIO.setup( m1_in3, GPIO.OUT )
    GPIO.setup( m1_in4, GPIO.OUT )

    # initializing
    GPIO.output( m1_in1, GPIO.LOW )
    GPIO.output( m1_in2, GPIO.LOW )
    GPIO.output( m1_in3, GPIO.LOW )
    GPIO.output( m1_in4, GPIO.LOW )

    motor_pins = [m1_in1,m1_in2,m1_in3,m1_in4]
    motor_step_counter = 0 
    cleanup(direction, motor_pins)
    exit( 0 )
    
def cleanup(direction, motor_pins):
    GPIO.output( m1_in1, GPIO.LOW )
    GPIO.output( m1_in2, GPIO.LOW )
    GPIO.output( m1_in3, GPIO.LOW )
    GPIO.output( m1_in4, GPIO.LOW )
    GPIO.cleanup()

    # the meat
    try:
        i = 0
        for i in range(step_count):
            for pin in range(0, len(motor_pins)):
                GPIO.output( motor_pins[pin], step_sequence[motor_step_counter][pin] )
            if direction==True:
                motor_step_counter = (motor_step_counter - 1) % 8
            elif direction==False:
                motor_step_counter = (motor_step_counter + 1) % 8
            else: # defensive programming
                print( "uh oh... direction should *always* be either True or False" )
                cleanup()
                exit( 1 )
            time.sleep( step_sleep )

    except KeyboardInterrupt:
        cleanup()
        exit( 1 )

    