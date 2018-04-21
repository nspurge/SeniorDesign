#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

import read
import lock
import query
import led
import SimpleMFRC522
import os

def main():

    tagId = read.readTag()
    count = query.userSearch(tagId)

    if (count == 1):
        if (os.path.isfile('/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt')):
            query.doorOpen(tagId)
            led.blinkGreen()
            sleep(.2)
            lock.openLock()
            os.rename('/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt', '/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt')
            led.greenOn()
            sleep(1.5)
        elif (os.path.isfile('/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt')):
            query.doorClose(tagId)
            led.blinkGreen()
            sleep(.2)
            lock.closeLock()
            os.rename('/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt', '/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt')
            led.greenOff()
            sleep(1.5)
    else:
        query.doNothing(tagId)
        led.blinkRed()
        sleep(1.5)
        pass

while True:
    main()
