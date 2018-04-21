#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

#Set GPIO Board numbering scheme
GPIO.setmode(GPIO.BCM)

#Set GPIO pin
servoPin = 18
GPIO.setup(servoPin, GPIO.OUT)

#Set pwm signal on pin to 50Hz
pwm = GPIO.PWM(servoPin, 50)
pwm.start(0) #set duty cycle to 0 so it doesn't cycle on startup

#function to set duty cycle as an angle
def setAngle(angle):
        servoPin = 18
        GPIO.setup(servoPin, GPIO.OUT)

        duty = angle / 18 + 2
        GPIO.output(servoPin, True)
        pwm.ChangeDutyCycle(duty)
        sleep(.5)
        GPIO.output(servoPin, False)
        pwm.ChangeDutyCycle(0)

#set function to open lock      
def openLock():
        pwm = GPIO.PWM(servoPin, 50)
        pwm.start(0)
        
        angle = 90
        setAngle(angle)
        pwm.stop()
        print 'lock opened'

#set function to close lock
def closeLock():
        pwm = GPIO.PWM(servoPin, 50)
        pwm.start(0)

        angle = 0
        setAngle(angle)
        pwm.stop()
        print 'lock closed'
