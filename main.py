import pygame as pg
import sys
import PIL

from color.Loader import Loader
from color.units.Point import Point

pg.init()


screen = pg.display.set_mode((1000, 1000))
fps = 1000
time = 0
clock = pg.time.Clock()
loader = Loader("units/rainbow_r.jpg")

points = []
start_point = Point(screen, loader,10, 10, 10)
points.append(start_point)
while True:
    time += 1 / fps

    if len(points) <= 1000000:
        points[len(points) - 1].draw()
        np = points[len(points) - 1].getNext(1/fps)
        print(f"new point x={np.x}, y={np.y}, z={np.z}")
        points.append(np)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    pg.display.flip()
    clock.tick(fps)

