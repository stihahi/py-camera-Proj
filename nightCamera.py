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
    p.add_argument('-e','--endHour', help="time the capture ends(24 hour)", type=int)
    p.add_argument('-i','--interval', help="capture interval time(sec) >3 sec", type=int)
    p.add_argument('-d','--directory', help="directory to save jpg files");
    args = p.parse_args()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(10,GPIO.OUT)
#    print args.endHour
    GPIO.output(10,True)
    dirname = args.directory
    try:
        os.mkdir(dirname)
    except:
        pass
    with picamera.PiCamera() as camera:
        try:
            for i, filename in enumerate(camera.capture_continuous(dirname+'/im{timestamp:%m%d%H%M%S}-{counter:03d}.jpg')):
                print(filename)
                time.sleep(3)
                GPIO.output(10,False)
                nowtime = datetime.datetime.now()
                if nowtime.hour > args.endHour:
                    break
                time.sleep(args.interval-6)
                GPIO.output(10,True)
                time.sleep(3)
        finally:
            pass

