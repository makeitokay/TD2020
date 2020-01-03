import pygame as pg

from core.settings import GAME_NAME, SCREEN_SIZE
from core.game import Game

pg.init()
screen = pg.display.set_mode(SCREEN_SIZE)
pg.display.set_caption(GAME_NAME)

game = Game(screen)
game.run()