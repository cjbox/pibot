import rrb3 as rrb
import time, random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

BATTERY_VOLTS = 9
MOTOR_VOLTS = 6

RightTrig = 40
RightEcho = 37

GPIO.setup(RightTrig, GPIO.OUT)
GPIO.setup(RightEcho, GPIO.IN)
GPIO.output(RightTrig, False)
time.sleep(0.5)

rr = rrb.RRB3(BATTERY_VOLTS, MOTOR_VOLTS)
TooClose = 15
NumberOfTurnsBeforeStopping = 10

def GetSideDistance(trig, echo):
	GPIO.output(trig, True)
	time.sleep(0.00001)
	GPIO.output(trig, False)

	pulse_start = time.time()
	
	while GPIO.input(echo)==0:
		pulse_start = time.time()
		print("pulse start")
		print(pulse_start)
	
	while GPIO.input(echo)==1:
		pulse_end = time.time()
		print("pulse end")
		print(pulse_end)

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)
	return distance

try:
	i=0
	while i<NumberOfTurnsBeforeStopping:
		rr.set_motors(0.5, 0, 0.5, 0)
		distance = rr.get_distance()
		while distance>TooClose:
			distance = rr.get_distance()
			time.sleep(0.1)
		print(distance)
		print("Right Sensor")
		rightDistance = GetSideDistance(RightTrig,RightEcho)
		print(rightDistance)
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