import pygame as pg
import sys

from Loader import Loader
from units.LorenzPoint import LorenzPoint
from units.RosselPoint import RosselPoint
from colors import *
pg.init()

"""constants"""
fps = 240
time = 0
screen = pg.display.set_mode((1000, 1000))
screen.fill(BLACK)
clock = pg.time.Clock()
loader = Loader("units/pattetns/purpleorange.jpg")


"""Dinamic"""
points = []
start_point = RosselPoint(screen, loader,10,10, 10)


"""main"""
points.append(start_point)
while True:
    time += 1 / fps

    if len(points) <= 1000000:
        points[len(points) - 1].draw()
        np = points[len(points) - 1].getNext(1/fps )
        points.append(np)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    pg.display.flip()
    clock.tick(fps)

