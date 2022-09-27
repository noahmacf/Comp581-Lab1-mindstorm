#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
left_motor = Motor(Port.B, positive_direction=Direction.CLOCKWISE)
right_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
#WHEEL_DIAMETER = 45
#AXLE_TRACK = 104
#robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
touch_sensor = TouchSensor(port = Port.S2)
ultrasonic_sensor = UltrasonicSensor(Port.S1)

# Lab code

# wait for button press
#brick.speaker.beep() # its ready
while not Button.CENTER in brick.buttons(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# move 1.2 meters
#robot.straight(1200) # move forward 1.2 meters
left_motor.run_time(800, 100, then=Stop.HOLD, wait=True)
right_motor.run_time(800, 100, then=Stop.HOLD, wait=True)
#brick.speaker.beep() # its finished

# wait for button press
while not Button.CENTER in brick.buttons(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# drive until wall is 50 cm away
while ultrasonic_sensor.distance > 500:
    #robot.drive(800, 0) # drives at a rate of 800 and angle of 0
    left_motor.run(800)
    right_motor.run(800)
#robot.stop()
left_motor.hold()
right_motor.hold()
#brick.speaker.beep() # its finished

# wait for button press
while not btn.Button.CENTER in brick.buttons(): # loops until button is pressed
    wait(10)  # Wait 0.01 second

# touch the surface
while not touch_sensor.pressed():
    #robot.drive(800, 0)
    left_motor.run(800)
#robot.stop()
left_motor.hold()
right_motor.hold()

# drive until wall is 50 cm away
while ultrasonic_sensor.distance < 500:
    #robot.drive(-800, 0) # drives backwards at a rate of 800 and angle of 0
    left_motor.run(-800)
    right_motor.run(-800)
#robot.stop()
left_motor.hold()
right_motor.hold()
#brick.speaker.beep() # its finished