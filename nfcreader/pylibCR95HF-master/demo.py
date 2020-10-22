#Import libraries
import RPi.GPIO as GPIO
import random
import os
import time

#Pins used
LED_green = 11
LED_red = 13
buzzer = 33
btnStart = 16
btnStop = 18
HIGH = 1
LOW = 0

valid = {12345: "SPRAGO001",6789: "EDWIAN004"}

def setup():
    GPIO.setmode(GPIO.BOARD)
    # Setup regular GPIO
    GPIO.setup(LED_green, GPIO.OUT)
    GPIO.setup(LED_red, GPIO.OUT)
    GPIO.setup(buzzer, GPIO.OUT)
    GPIO.setup(btnStart, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(btnStop, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LED_red, HIGH)
    # Setup PWM channels
    #pwmBuzz = GPIO.PWM(buzzer,100)
   # pwmBuzz.start(0)
    # Setup debouncing and callbacks
    #GPIO.add_event_detect(btnStart, GPIO.FALLING, callback=btnStart_pressed, bouncetime=300)
    #GPIO.add_event_detect(btnStop, GPIO.FALLING, callback=btnStop_pressed, bouncetime=300)

#def btnStart_pressed(channel):


def beep(delay):
    GPIO.output(LED_red, LOW)
    GPIO.output(LED_green, HIGH)
    GPIO.output(buzzer, HIGH)
    time.sleep(delay)
    GPIO.output(buzzer, LOW)
    GPIO.output(LED_red, HIGH)
    GPIO.output(LED_green, LOW)
        
    

if __name__ == "__main__":
    try:
        setup()
        #time.sleep(2)
        beep(0.5)
        
            #print("set GIOP high")
            
       # main()            
    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
        print("Keyboard interrupt")


    finally:
        print("clean up") 
        GPIO.cleanup() # cleanup all GPIO 
   


