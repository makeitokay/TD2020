import pygame as pg
from os import path
import json

from .settings import GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT

# Colors

BLACK = pg.Color("BLACK")
WHITE = pg.Color("WHITE")
BLUE = pg.Color(0, 255, 255)
GOLD = pg.Color(255, 223, 0)
RED = pg.Color("RED")


# Useful functions

def terminate():
    pg.quit()
    exit()


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pg.image.load(fullname).convert_alpha()


def scale_image(image, coefficient):
    width, height = int(image.get_width() * coefficient), int(image.get_height() * coefficient)
    return pg.transform.scale(image, (width, height))


def load_level(number):
    fullname = path.join("data", "levels", str(number) + ".txt")
    level = [["*" for _ in range(GAME_FIELD_WIDTH)] for __ in range(GAME_FIELD_HEIGHT)]
    with open(fullname) as f:
        level_data = [row.strip() for row in f]
    for i in range(len(level_data)):
        for j in range(len(level_data[i])):
            level[i][j] = level_data[i][j]
    return level


def load_waves(number):
    fullname = path.join("data", "levels", "waves", str(number) + ".json")
    with open(fullname) as f:
        return json.load(f)


def get_center_distance_from_way(rect1, rect2, way):
    dx = abs(rect1.center[0] - rect2.center[0])
    dy = abs(rect1.center[1] - rect2.center[1])
    if way in (">", "<"):
        return dx
    return dy