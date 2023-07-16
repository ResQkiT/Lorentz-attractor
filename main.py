import pygame as pg
import sys

from datetime import datetime
from Loader import Loader
from units.LorenzPoint import LorenzPoint
from units.RosselPoint import RosselPoint
from units.NAttractorPoint import NAttractorPoint
from colors import *
pg.init()

"""constants"""
fps = 100000
time = 0
screen = pg.display.set_mode((1000, 1000))
screen.fill(BLACK)
clock = pg.time.Clock()
loader = Loader("units/pattetns/rainbow_r.jpg")


"""Dinamic"""
points = []
start_point = NAttractorPoint(screen, loader,0,0, 0)


"""main"""
points.append(start_point)
while True:
    time += 1 / fps

    if len(points) <= 1000000:
        #points[len(points) - 1].draw()
        np = points[len(points) - 1].getNext(1/60 )
        points.append(np)
        np.draw()
        #points.pop(0)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            print("Скриншот")
            pg.image.save(screen,"screenshots//" + str(datetime.now().time()).replace(":", "_").replace(".", "_")+"__" + str(hash(np)) + '.png')

    pg.display.flip()
    clock.tick(fps)

