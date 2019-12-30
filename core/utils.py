import pygame as pg
from os import path
from .settings import CELL_SIZE

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