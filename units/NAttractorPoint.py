import math

import pygame as pg

class NAttractorPoint:
    def __init__(self, screen,loader, x, y, z , radius = 0):
        self.screen = screen
        self.loader = loader

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.c0 = 1.6831349342542232
        self.c1 = -2.9984035545418575
        self.c2 = 2.1207267208634164
        self.c3 = -2.121518002564899

        self.k = 75
        self.color = loader.getColor(int(z) * self.k * 2)

    def getNextX(self):
        c0 = self.c0
        c1 = self.c1
        y = self.y
        x = self.x
        return c0 * math.sin(y - y*(y**2 + 1) / 2) + c1 * math.tanh(x - x * (x**2 +1) / 2)
    def getNextY(self):
        c2 = self.c2
        c3 = self.c3
        y = self.y
        x = self.x
        return c2*math.sin(x - x*(x**2 +1) / 2) + c3/(math.cosh(y - y*(y**2 +1) / 2))

    def getNextZ(self):
        return math.sqrt(self.x ** 2 + self.y**2)

    def draw(self):
        pg.draw.circle(self.screen, self.color, (int(self.x *self.k+ 500) ,int( self.y * self.k+ 500)), self.radius )

    def getNext(self, deltaTime):
        return NAttractorPoint(self.screen,
                               self.loader,
                               self.getNextX(),
                               self.getNextY(),
                               self.getNextZ())
        pass
