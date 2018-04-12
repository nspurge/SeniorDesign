#!/usr/bin/env python

import RPi.GPIO as GPIO

import read
import lock
#import mysql

def main():
    
    try:
        read.readTag()
        lock.openLock()
        lock.closeLock()
    finally:
        print 'fin'
        GPIO.cleanup()

main()
