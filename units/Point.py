import math

import pygame as pg

from color.colors import *

pg.init()

class Point:

    def __init__(self, screen,loader, x, y, z , radius = 1):
        self.screen = screen
        self.loader = loader

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.b = 8/3
        self.s = 10
        self.r = 28

        self.k = 15
        self.color = loader.getColor(int(z) * self.k * 2)


    def getDeltaX(self):
        return -self.s * self.x + self.s * self.y


    def getDeltaY(self):
        return -self.x * self.z + self.r * self.x - self.y


    def getDeltaZ(self):
        return self.x * self.y - self.b * self.z


    def draw(self):
        pg.draw.circle(self.screen, self.color, (int(self.x *self.k+ 500) ,int( self.y * self.k+ 500)), self.radius )


    def getNext(self, deltaTime):
        return Point(self.screen,
                     self.loader,
                    self.x + self.getDeltaX() * deltaTime,
                    self.y + self.getDeltaY() * deltaTime,
                    self.z + self.getDeltaZ() * deltaTime)