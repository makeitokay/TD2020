import pygame as pg
import random

from core.settings import GAME_NAME, SCREEN_SIZE

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(GAME_NAME)
clock = pg.time.Clock()

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

while True:
    screen.fill(color)
    pg.display.update()
    clock.tick(5)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
