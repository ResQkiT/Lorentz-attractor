import math

import pygame as pg
from units.Point import Point
from Loader import Loader

class NAttractorPoint:
    def __init__(self, screen, radius = 0):
        self.screen = screen
        self.radius = radius

        self.c0 = 1.6831349342542232
        self.c1 = -2.9984035545418575
        self.c2 = 2.1207267208634164
        self.c3 = -2.121518002564899

        self.k = 75

    def getNextX(self,x, y, z):
        c0 = self.c0
        c1 = self.c1
        return c0 * math.sin(y - y*(y**2 + 1) / 2) + c1 * math.tanh(x - x * (x**2 +1) / 2)
    def getNextY(self,x, y, z):
        c2 = self.c2
        c3 = self.c3
        return c2*math.sin(x - x*(x**2 +1) / 2) + c3/(math.cosh(y - y*(y**2 +1) / 2))

    def getNextZ(self,x, y, z):
        return math.sqrt(x ** 2 + y**2)

    def draw(self,x, y, z):
        color = Loader.getColor(int(z) * self.k * 2)
        pg.draw.circle(self.screen, color, (int(x * self.k + 500), int(y * self.k + 500)), self.radius)
    def getNext(self,x,y,z, deltaTime):
        return Point(self.getNextX(x,y,z), self.getNextY(x,y,z), self.getNextZ(x,y,z), self)

