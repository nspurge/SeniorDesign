#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

import read
import lock
#import mysql

#Set GPIO Board numbering scheme
GPIO.setmode(GPIO.BCM)

def main():
    
    read.readTag()
    sleep(1)
    lock.closeLock()
    GPIO.cleanup()

main()
