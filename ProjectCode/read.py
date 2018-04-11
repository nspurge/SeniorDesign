#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def readTag():
	try:
		id, text = reader.read()
		print (id)
		return (text)
	finally:
		GPIO.cleanup()
