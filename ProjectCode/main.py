#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

import read
import lock
import query
import SimpleMFRC522
import os

def main():

    tagId = read.readTag()
    count = query.userSearch()

    if (count == 1):
        if (os.path.isfile('/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt')):
            print '4'
#            query.doorOpen()
            lock.openLock()
            GPIO.cleanup()
            os.rename('/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt', '/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt')
        elif (os.path.isfile('/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt')):
            print '5'
#            query.doorClose()
            lock.closeLock()
            GPIO.cleanup()
            os.rename('/home/pi/Desktop/SeniorDesign/ProjectCode/opened.txt', '/home/pi/Desktop/SeniorDesign/ProjectCode/closed.txt')
    else:
        print 'Blink Red LED '
        pass

main()
