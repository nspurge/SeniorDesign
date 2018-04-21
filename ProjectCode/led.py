import RPi.GPIO as GPIO
from time import sleep

def blinkGreen():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    
    GPIO.output(16, GPIO.HIGH)
    sleep(.2)
    GPIO.output(16, GPIO.LOW)
    sleep(.2)
    GPIO.output(16, GPIO.HIGH)
    sleep(.2)
    GPIO.output(16, GPIO.LOW)
    sleep(.2)
    GPIO.output(16, GPIO.HIGH)
    sleep(.2)
    GPIO.output(16, GPIO.LOW)

def blinkRed():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.OUT)
    
    GPIO.output(26, GPIO.HIGH)
    sleep(.2)
    GPIO.output(26, GPIO.LOW)
    sleep(.2)
    GPIO.output(26, GPIO.HIGH)
    sleep(.2)
    GPIO.output(26, GPIO.LOW)
    sleep(.2)
    GPIO.output(26, GPIO.HIGH)
    sleep(.2)
    GPIO.output(26, GPIO.LOW)

def greenOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)
    
    GPIO.output(16, GPIO.HIGH)
    
def greenOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(16, GPIO.OUT)

    GPIO.output(16, GPIO.LOW)
