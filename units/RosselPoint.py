import math

import pygame as pg

from color.colors import *

pg.init()

class RosselPoint:
    def __init__(self, screen, loader, x, y, z, radius=0):
        self.screen = screen
        self.loader = loader

        self.x = x
        self.y = y
        self.z = z
        self.radius = radius

        self.a = 0.2
        self.b = 0.2
        self.c = 14

        self.k = 15
        self.color = loader.getColor(int(z) * self.k + 500)

    def getDeltaX(self):
        return -self.y - self.z

    def getDeltaY(self):
        return self.x + self.a * self.y

    def getDeltaZ(self):
        return self.b + self.z * (self.x - self.c)

    def draw(self):
        pg.draw.circle(self.screen, self.color, (int(self.x * self.k + 500), int(self.y * self.k + 500)), self.radius)

    def getNext(self, deltaTime):
        return RosselPoint(self.screen,
                           self.loader,
                           self.x + self.getDeltaX() * deltaTime,
                           self.y + self.getDeltaY() * deltaTime,
                           self.z + self.getDeltaZ() * deltaTime)