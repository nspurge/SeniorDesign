#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def readTag():
        id, tagId = reader.read()
        print tagId
        return (tagId)

readTag()
