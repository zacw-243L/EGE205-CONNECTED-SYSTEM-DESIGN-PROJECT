import time
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P9_15", GPIO.IN)

while True:
    if GPIO.input("P9_15"):
        print("No Motion is Detected")
    else:
        print("Motion is Detected")
    time.sleep(0.3)
