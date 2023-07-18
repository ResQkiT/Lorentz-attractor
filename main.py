import pygame as pg
import sys

from datetime import datetime
from Loader import Loader
from units.LorenzPoint import LorenzPoint
from units.Point import Point
from units.RosselPoint import RosselPoint
from units.NAttractorPoint import NAttractorPoint
from colors import *
pg.init()

"""constants"""
fps = 5000
time = 0
screen = pg.display.set_mode((1000, 1000))
screen.fill(BLACK)
clock = pg.time.Clock()
Loader.init("units/pattetns/rainbow_r.jpg")

"""Dinamic"""

start_point = Point(1,1, 1, LorenzPoint(screen), True)
pointsCount = 1

"""main"""

while True:
    time += 1 / fps

    if pointsCount <= 1000000:

        np = start_point.getNext(1/fps)
        print(np.isDrawAble())
        if np.isDrawAble():
            np.draw()
            print(" рисую")
        else:
            print("не рисую")
        start_point = np
        pointsCount += 1
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            print("Скриншот")
            pg.image.save(screen,"screenshots//" + str(datetime.now().time()).replace(":", "_").replace(".", "_")+"__" + str(hash(np)) + '.png')

    pg.display.flip()
    clock.tick(fps)

