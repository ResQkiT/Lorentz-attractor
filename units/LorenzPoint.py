import pygame as pg

from units.Point import Point
from Loader import Loader

pg.init()


class LorenzPoint:
    def __init__(self, screen, radius=0):
        self.screen = screen
        self.radius = radius

        self.b = 8 / 3
        self.s = 10
        self.r = 28

        self.k = 15
        # self.color = loader.getColor(int(z) * self.k * 2)

    def getDeltaX(self, x, y, z):
        return -self.s * x + self.s * y

    def getDeltaY(self, x, y, z):
        return -x * z + self.r * x - y

    def getDeltaZ(self, x, y, z):
        return x * y - self.b * z

    def draw(self, x, y, z):
        color = Loader.getColor(z)
        pg.draw.circle(self.screen, color, (int(x * self.k + 500), int(y * self.k + 500)), self.radius)

    def getNext(self, x, y, z, deltaTime):
        return Point(x + self.getDeltaX() * deltaTime,
                     y + self.getDeltaY() * deltaTime,
                     z + self.getDeltaZ() * deltaTime)
