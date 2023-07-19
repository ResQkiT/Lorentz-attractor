import math

import pygame as pg

from units.Point import Point
from Loader import Loader

pg.init()

class RosselPoint:
    def __init__(self, screen, radius=0):
        self.screen = screen
        self.radius = radius

        self.a = 0.2
        self.b = 0.2
        self.c = 14

        self.k = 15

    def getDeltaX(self, x, y, z):
        return -y - z

    def getDeltaY(self, x, y, z):
        return x + self.a * y

    def getDeltaZ(self, x, y, z):
        return self.b + z * (x - self.c)

    def draw(self, x, y, z):
        color = Loader.getColor(int(z) * self.k )
        pg.draw.circle(self.screen, color, (int(x * self.k + 500), int(y * self.k + 500)), self.radius)

    def getNext(self,x,y,z, deltaTime):
        dx = self.getDeltaX(x, y, z)
        dy = self.getDeltaY(x, y, z)
        dz = self.getDeltaZ(x, y, z)
        a = [dx, dy, dz]

        if any(list(map(lambda x: abs(x) < 100, a))):
            dx, dy, dz = list(map(lambda x: x * 20, a))

        return Point(x + dx * deltaTime,
                     y + dy * deltaTime,
                     z + dz * deltaTime,
                     self)