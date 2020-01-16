from core.objects.gameobject import GameObject
from core.objects.platforms.road import Road

import pygame as pg


class Enemy(GameObject):
    IMAGE = None

    SPRITE_GROUPS = ["enemies"]

    HP_BAR_LENGTH = 30
    HP_BAR_HEIGHT = 7

    MAX_HP = 0

    def __init__(self, game, pos):
        super().__init__(game, pos=pos)

        self.current_way = None

        self.hp = 0

    def update(self):
        self.current_cell = self.game.game_field.get_cell_obj(self.game.game_field.get_cell((self.pos)))
        if isinstance(self.current_cell, Road):
            # Если текущее направление по оси X, то нас интересует только dx между мобом и клеткой
            if self.current_way in (">", "<"):
                distance = self.get_x_center_distance(self.current_cell)
            else:
                distance = self.get_y_center_distance(self.current_cell)
            # Расстояние между центрами проверяется для того, чтобы моб поворачивал примерно по центру клетки
            if distance < 5:
                self.current_way = self.current_cell.way
        else:
            self.current_way = self.game.spawn_platform.get_way_to_road()

        dx, dy = Road.WAYS[self.current_way]
        self.rect.x += dx
        self.rect.y += dy

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def draw_hp_bar(self):
        length = 30
        fill = (self.hp / self.MAX_HP) * length
        outline_rect = pg.Rect(self.rect.x, self.rect.y - 10, self.HP_BAR_LENGTH, self.HP_BAR_HEIGHT)
        fill_rect = pg.Rect(self.rect.x, self.rect.y - 10, fill, self.HP_BAR_HEIGHT)
        pg.draw.rect(self.game.surface, pg.Color("GREEN"), fill_rect)
        pg.draw.rect(self.game.surface, pg.Color("WHITE"), outline_rect, 2)