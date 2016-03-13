import RPi.GPIO as GPIO
import time

PW_PIN = 16
SV1 = 19
SV2 = 26

GPIO.setmode(GPIO.BCM)

GPIO.setup(PW_PIN,GPIO.OUT)
GPIO.setup(SV1,GPIO.OUT)
GPIO.setup(SV2,GPIO.OUT)

GPIO.output(PW_PIN,True)

sv1 = GPIO.PWM(SV1,50)

sv1.start(20)
time.sleep(0.5)

time.sleep(3)
sv1.ChangeDutyCycle(50)
time.sleep(0.5)

time.sleep(3)
sv1.ChangeDutyCycle(100)
time.sleep(0.5)
sv1.stop()
GPIO.cleanup()


def calc_duty(angle):
    return (1.0+angle/180.0) / 20.0 * 100.0
