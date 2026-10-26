#!/usr/bin/env python3
#
#  search.py
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

class Search:
    def __init__(self):
        self.angle = 90
    def find_angle(self,cx):
        if cx is None:
            return self.angle
        if cx< 220:
            self.angle -=5
        elif cx> 420:
            self.angle +=5
            
        self.angle = max(0, min(180, self.angle))
        return self.angle
