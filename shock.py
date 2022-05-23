import RPi.GPIO as GPIO

import time

# GPIO pin number of LED
LED = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(LED, GPIO.OUT)
print("Shock on")
GPIO.output(LED, GPIO.HIGH)
time.sleep(1)
print("Shock off")
GPIO.output(18, GPIO.LOW)
