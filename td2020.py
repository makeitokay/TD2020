import pygame as pg
import random

from core.settings import GAME_NAME, SCREEN_SIZE
from core.game import Game

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(GAME_NAME)
clock = pg.time.Clock()

game = Game(screen)
game.run()