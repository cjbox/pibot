import time, random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

Left = 4
Centre = 18
Right = 17
Counter = 0

GPIO.setup(Centre, GPIO.IN)
GPIO.setup(Left, GPIO.IN)
GPIO.setup(Right, GPIO.IN)

try:
	while Counter<10:
		print("--")
		line = GPIO.input(Left)
		print(line)
		line = GPIO.input(Centre)
		print(line)
		line = GPIO.input(Right)
		print(line)
		time.sleep(5)
		Counter+=1

finally:
    print("Exiting")
#	GPIO.cleanup()