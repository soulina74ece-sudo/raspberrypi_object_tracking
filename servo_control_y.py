#!/usr/bin/env python3
#
#  servo_control_y.py
#  
#  Copyright 2026 Unknown <lab@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Servo:
    def __init__(self, pin):
        self.pin= pin
        GPIO.setup(self.pin, GPIO.OUT)
        self.pwm =GPIO.PWM(self.pin, 50)
        self.pwm.start(0)
    def move(self, angle):
        angle= max(0, min(180, angle))
        duty = 2+ (angle/18)
        
        self.pwm.ChangeDutyCycle(duty)
        time.sleep(0.02)
        self.pwm.ChangeDutyCycle(0)
        
    def release(self):
        self.pwm.stop()
    
    @staticmethod
    def cleanup():
        GPIO.cleanup()
