#!/usr/bin/env python
# -*- coding: utf-8 -*-

import picamera
import time
import RPi.GPIO as GPIO
import datetime
import argparse
import os

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument('-d','--dHour', help="duration of the capture (hour)", type=int, default=10)
    p.add_argument('-i','--interval', help="capture interval time(sec) >3 sec", type=int, default=60)
    args = p.parse_args()
    POW_PIN=16
    SV1=19
    SV2=26
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(POW_PIN,GPIO.OUT)
#    print args.endHour
    GPIO.output(POW_PIN,True)
    dirname = datetime.date.today().strftime("%y%m%d")
    stopTime = datetime.datetime.now() + datetime.timedelta(hours=args.dHour)
    try:
        os.mkdir(dirname)
    except:
        pass
    with picamera.PiCamera() as camera:
        try:
            for i, filename in enumerate(camera.capture_continuous(dirname+'/im{timestamp:%H%M%S}-{counter:03d}.jpg')):
                print(filename)
                time.sleep(3)
                GPIO.output(POW_PIN,False)
                nowTime = datetime.datetime.now()
                t_delta = stopTime-nowTime
                if t_delta.seconds > 0:
                    break
                time.sleep(args.interval-6)
                GPIO.output(POW_PIN,True)
                time.sleep(3)
        finally:
            pass
