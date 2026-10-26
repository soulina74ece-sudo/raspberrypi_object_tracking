#!/usr/bin/env python3
#
#  untitled.py
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
from picamera2 import Picamera2
import cv2 
import time

class Camera:
    def __init__(self):
        self.camera= Picamera2()
        config= self.camera.create_preview_configuration(
        main={"size": (640, 480)})
        
        self.camera.configure(config)
        self.camera.start()
        time.sleep(2)
        
    def get_frame(self):
           frame= self.camera.capture_array()
           frame= cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
           return frame

    def release(self):
            self.camera.stop()
            
