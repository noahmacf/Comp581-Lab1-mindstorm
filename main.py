#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

#pseudocode

#while(program is running)
#ev3 = EV3brick()
#start_distance = us_sensor.distance()
#target_distance = us_sensor.distance() - 1200

#if(button is pressed)
#while(us_sensor.distance() < target_distance)
#motor1.run(180)
#motor2.run(180)

#if(us_sensor.distance() == target_distance)
#motor1.brake()
#motor2.brake()
#ev3.speaker.beep()

#if(button is pressed again)
#while(us_sensor.distance() > 500)
#motor1.run(180)
#motor2.run(180)

#if(us_sensor.distance() == 500)
#motor1.brake()
#motor2.brake()
#ev3.speaker.beep()

#if(button press again)
#		motor1.run(180)
#motor2.run(180)
#	if(touch_sensor.pressed())
#		motor1.brake()
#		motor2.brake()
#		while(us_sensor.distance() < 500)
#			motor1.run(-180)
#`			motor2.run(-180)
#				if(us_sensor.distance() == 500)
#                   motor1.brake()
#                   motor2.brake()



# Create your objects here.
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
WHEEL_DIAMETER = 55
AXLE_TRACK = 104
robot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
touch_sensor = TouchSensor(port = Port.S1)
ultrasonic_sensor = UltrasonicSensor(Port.S3)
button_pressed = Button.CENTER in EV3Brick.buttons

# Example code
ev3.speaker.beep()

motor1 = Motor(port = Port.B, positive_direction = Direction.COUNTERCLOCKWISE)

motor1.run(speed = 180)
motor1.run_target(speed = 180, target_angle = 360, then=Stop.HOLD, wait = True)
motor1.brake()

touch_sensor = TouchSensor(port = Port.S1)

touch_sensor.pressed()

# Lab code

# wait for button press
ev3.speaker.beep() # its ready
while not btn.any(): # loops until button is pressed
    sleep(0.01)  # Wait 0.01 second

# move 1.2 meters
robot.straight(1200) # move forward 1.2 meters
ev3.speaker.beep() # its finished

# wait for button press
while not btn.any(): # loops until button is pressed
    sleep(0.01)  # Wait 0.01 second

# drive until wall is 50 cm away
while ultrasonic_sensor.distance > 500:
    robot.drive(800, 0) # drives at a rate of 800 and angle of 0
robot.stop()
ev3.speaker.beep() # its finished

# wait for button press
while not btn.any(): # loops until button is pressed
    sleep(0.01)  # Wait 0.01 second

# touch the surface
while not touch_sensor.pressed():
    robot.drive(800, 0)
robot.stop()

# drive until wall is 50 cm away
while ultrasonic_sensor.distance < 500:
    robot.drive(-800, 0) # drives backwards at a rate of 800 and angle of 0
robot.stop()
ev3.speaker.beep() # its finished