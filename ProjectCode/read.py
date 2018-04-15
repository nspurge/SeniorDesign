#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

def readTag():
        print 'run'
        id, tagId = reader.read()
        print 'done'
        return (tagId)
        print (tagId)

readTag()

