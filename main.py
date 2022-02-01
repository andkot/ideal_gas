import numpy as np
import cv2

class Box:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

class Point:
    def __init__(self, r, x=0, y=0, vx=0, vy=0):
        self.r = r
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def interract(self, obj):
        if obj.type == 'box':
            result = interract_wall(self, obj)
        elif obj.type == 'point':
            result = interract_point(self, obj)
        return result

    def interract_wall(self, box):



    