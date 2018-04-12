#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

#Set GPIO Board numbering scheme
#GPIO.setmode(GPIO.BOARD)

#Set GPIO pin
#GPIO.setup(12, GPIO.OUT)
#Set pwm signal on pin to 50Hz
#pwm = GPIO.PWM(12, 50)
#pwm.start(0) #set duty cycle to 0 so it doesn't cycle on startup

#function to set duty cycle as an angle
def setAngle():
	duty = angle / 18 + 2
	GPIO.output(12, True)
	pwm.ChangeDutyCycle(duty)
	sleep(1)
	GPIO.output(12, False)
	pwm.ChangeDutyCycle(0)

#set function to open lock	
def openLock():
	print "opening lock"
#	setAngle(90)
#	pwm.stop()
#	GPIO.cleanup()

#set function to close lock
def closeLock():
	print "closing lock"
#	setAngle(0)
#	pwm.stop()
#	GPIO.cleanup()
