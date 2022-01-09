import RPi.GPIO as GPIO
import time

def off():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12,50)
    p.start(7.5)
    p.ChangeDutyCycle(4.2)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.stop()
    GPIO.cleanup()

def on():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12,50)
    p.start(7.5)
    p.ChangeDutyCycle(4.2)
    time.sleep(1)
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.stop()
    GPIO.cleanup()
