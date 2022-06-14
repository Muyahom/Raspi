import serial
import time
import re
import RPi.GPIO as GPIO

test = serial.Serial("/dev/ttyACM0", baudrate = 115200)
door_password = "91759999"
while 1:
    
    time.sleep(3)
    a = test.readline().rstrip()
    pwd = a.decode("utf-8")
    
    print(pwd)
    
    if door_password == pwd: # if password 5 and matched suc activate
            print("Success")
            GPIO.setmode(GPIO.BCM)
            
            GPIO.setwarnings(False)
            GPIO.setup(17, GPIO.OUT)

            print("Open")
            GPIO.output(17, GPIO.LOW)
            time.sleep(1)
            GPIO.output(17, GPIO.HIGH)
            time.sleep(7)

            print("close")
            GPIO.output(17, GPIO.LOW)
            time.sleep(1)

            GPIO.output(17, GPIO.HIGH)
            time.sleep(7)
            GPIO.cleanup
            
            break
            


