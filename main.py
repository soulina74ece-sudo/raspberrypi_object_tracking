#!/usr/bin/env python3
#
#  main.py
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


from camera import Camera
from object_detection import ObjectDetector
from servo_control import Servo
import cv2

camera =Camera()
detector =ObjectDetector()
servo =Servo()

current_angle= 90
servo.move(current_angle)
FRAME_CENTER =320
DEAD_ZONE =20
STEP= 2

try:
    while True:
        frame =camera.get_frame()
        frame,cx,cy= detector.detect(frame)
        if cx is not None:
            if cx <FRAME_CENTER - DEAD_ZONE:
                current_angle+ min(180, current_angle + STEP)
                servo.move(current_angle)
            elif cx> FRAME_CENTER + DEAD_ZONE:
                current_angle = max(0, current_angle -STEP)
                servo.move(current_angle)
                cv2.imshow("Object Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
finally:
    camera.release()
    servo.release()
    cv2.destroyAllWindows()
