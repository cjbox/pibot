import rrb3 as rrb
import time, random

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

rr = rrb.RRB3(BATTERY_VOLTS, MOTOR_VOLTS)
TooClose = 15
NumberOfTurnsBeforeStopping = 10

try:
	i=0
	while i<NumberOfTurnsBeforeStopping:
		rr.set_motors(0.5, 0, 0.5, 0)
		distance = rr.get_distance()
		while distance>TooClose:
			distance = rr.get_distance()
			time.sleep(0.1)
		print(distance)
		dl = random.randint(0, 1)
		if dl == 0:
			dr = 1
		else:
			dr = 0
		rr.set_motors(1, dr, 1, dl)
		time.sleep(0.2)
		i += 1
finally:
    rr.set_motors(0, 0, 0, 0)
    print("Exiting")
    rr.cleanup()