#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
left_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
touch_sensor = TouchSensor(port = Port.S2)
ultrasonic_sensor = UltrasonicSensor(port = Port.S1)
SPEED = 100
LEFTFACTOR = 1.01750
BACKWARDS = -100
METERTIME = 8330

# Lab code

# wait for button press
while not Button.CENTER in brick.buttons(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# move 1.2 meters
left_motor.run_time(400 * LEFTFACTOR, METERTIME, then=Stop.HOLD, wait=False)
right_motor.run_time(400, METERTIME, then=Stop.HOLD, wait=True)
brick.sound.beep() # its finished

# wait for button press
while not EV3Brick.buttons.pressed(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# drive until wall is 50 cm away
while not ultrasonic_sensor.distance() < 527:
    left_motor.run(SPEED * LEFTFACTOR)
    right_motor.run(SPEED)
left_motor.hold()
right_motor.hold()
brick.sound.beep() # its finished

# wait for button press
while not EV3Brick.buttons.pressed(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# touch the surface
while not touch_sensor.pressed():
    left_motor.run(SPEED * LEFTFACTOR)
    right_motor.run(SPEED)
left_motor.hold()
right_motor.hold()

# drive until wall is 50 cm away
while not ultrasonic_sensor.distance() > 527:
    left_motor.run(BACKWARDS * LEFTFACTOR)
    right_motor.run(BACKWARDS)
left_motor.hold()
right_motor.hold()