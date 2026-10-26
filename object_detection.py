#!/usr/bin/env python3
#
#  object_detection.py
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

import cv2
import numpy as np

class ObjectDetector:
    def __init__(self):
        self.lower_blue= np.array([100, 150, 50])
        self.upper_blue= np.array([140, 255, 255])
    def detect(self, frame):
        hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask= cv2.inRange(hsv, self.lower_blue, self.upper_blue)
        cv2.imshow("Mask", mask)
        kernel= np.ones((5,5), np.uint8)
        mask= cv2.erode(mask, kernel, iterations=1)
        mask= cv2.dilate(mask, kernel, iterations=2)
        contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("Contours:", len(contours))
        cx = None
        cy= None
        if len(contours)>0:
            largest = max(contours, key= cv2.contourArea)
            if cv2.contourArea(largest)>500:
                x,y,w,h = cv2.boundingRect(largest)
                cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
                
                M= cv2.moments(largest)
                if M["m00"]!=0:
                    cx = int(M["m10"]/ M["m00"])
                    cy = int(M["m01"]/ M["m00"])
                    
                cv2.circle(frame, (cx,cy),5, (0,0,255),-1)
                cv2.putText(frame,f"({cx},{cy})", (cx+10,cy-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)
        return frame, cx, cy
