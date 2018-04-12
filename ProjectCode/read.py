#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def readTag():
        try:
#                id, tagId = reader.read()
#                print (id)
#                print (tagId)
                print "howdy"
        finally:
                GPIO.cleanup()
