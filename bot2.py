import rrb3 as rrb
import time, random
import RPI.GPIO as GPIO

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

rr = rrb.RRB3(BATTERY_VOLTS, MOTOR_VOLTS)
TooClose = 15
NumberOfTurnsBeforeStopping = 10

Centre = 31
Left = 32
Right = 33

GPIO.setup(Centre, GPIO.IN)
GPIO.setup(Left, GPIO.IN)
GPIO.setup(Right, GPIO.IN)

try:
	distance = rr.get_distance()
	while distance>TooClose:
		rr.set_motors(0.5, 0, 0.5, 0)
		line_left = GPIO.input(Left)
		line_right = GPIO.input(Right)
		
		if line_left == 0:
			rr.set_motors(0, 0, 0.5, 0)
			time.sleep(1)
			rr.set_motors(0.5, 0, 0.5, 0)
			time.sleep(0.5)
		elif line_right == 0:
			rr.set_motors(0.5, 0, 0, 0)
			time.sleep(1)
			rr.set_motors(0.5, 0, 0.5, 0)
			time.sleep(0.5)
		else:
			rr.set_motors(0.5, 0, 0.5, 0)

finally:
    rr.set_motors(0, 0, 0, 0)
    print("Exiting")
    rr.cleanup()
	GPIO.cleanup()