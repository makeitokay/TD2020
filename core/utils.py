import pygame as pg
from os import path
from .settings import CELL_SIZE, FIELD_WIDTH, FIELD_HEIGHT

# Colors

BLACK = pg.Color("BLACK")
WHITE = pg.Color("WHITE")
BLUE = pg.Color(0, 255, 255)


# Useful functions

def terminate():
    pg.quit()
    exit()


def load_image(filename):
    fullname = path.join("data", "images", filename)
    return pg.image.load(fullname).convert_alpha()


def get_cell_coordinates(x, y):
    return x * CELL_SIZE, y * CELL_SIZE


def load_level(number):
    fullname = path.join("data", "levels", str(number) + ".txt")
    level = [["*" for _ in range(FIELD_WIDTH)] for __ in range(FIELD_HEIGHT)]
    with open(fullname) as f:
        level_data = [row.strip() for row in f]
    for i in range(len(level_data)):
        for j in range(len(level_data[i])):
            level[i][j] = level_data[i][j]
    return level
