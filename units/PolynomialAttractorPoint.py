import math

import pygame as pg

from units.Point import Point
from Loader import Loader

pg.init()

class PolynomialAttractorPoint:
    def __init__(self, screen, pattern, radius=0):
        self.screen = screen
        self.radius = radius

        self.odds = self.initOdds(pattern)
        print(self.odds)
        self.k = 500
    def initOdds(self, pattern):
        odds = []
        for letter in pattern:
            n = ord(letter.lower()) - ord('a')
            c = -12 + n
            odds.append(c/10)

        return odds

    def getNextX(self, x, y, z):
        ods = self.odds
        nx = ods[0] + ods[1] * x + ods[2] * x**2 + ods[3] * x * y + ods[4] * y + ods[5] * y ** 2

        return nx

    def getNextY(self, x, y, z):
        ods = self.odds
        ny = ods[6] + ods[7] * x + ods[8] * x ** 2 + ods[9] * x * y + ods[10] * y + ods[11] * y ** 2

        return ny

    def getNextZ(self, x, y, z):
        return (x + y)

    def draw(self, x, y, z):
        color = Loader.getColor(int(z) * self.k * 2 )
        pg.draw.circle(self.screen, color, (int(x * self.k  ), int(y * self.k + 1000)), self.radius)

    def getNext(self, x, y, z, deltaTime):
        return Point(self.getNextX(x, y, z), self.getNextY(x, y, z), self.getNextZ(x, y, z), self)
