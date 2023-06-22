import pygame as pg
import sys

from Loader import Loader
from units.LorenzPoint import LorenzPoint
from units.RosselPoint import RosselPoint

pg.init()


"""constants"""
fps = 100000
time = 0
screen = pg.display.set_mode((1000, 1000))
clock = pg.time.Clock()
loader = Loader("units/rainbow_r.jpg")


"""Dinamic"""
points = []
start_point = RosselPoint(screen, loader,0,0, 1)


"""main"""
points.append(start_point)
while True:
    time += 1 / fps

    if len(points) <= 1000000:
        points[len(points) - 1].draw()
        np = points[len(points) - 1].getNext(1/30 )
        #print(f"new point x={np.x}, y={np.y}, z={np.z}")
        points.append(np)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    pg.display.flip()
    clock.tick(fps)

