from core.objects.gameobject import GameObject
from core.objects.platforms.road import Road
from core.utils import LEFT, RIGHT, WHITE, GREEN, RED, GOLDENROD

import pygame as pg


class Enemy(GameObject):
    IMAGE = None

    SPRITE_GROUPS = ["enemies"]

    HP_BAR_LENGTH = 30
    HP_BAR_HEIGHT = 7

    MAX_HP = 0

    def __init__(self, game, hardness, pos):
        super().__init__(game, pos=pos)

        self.current_way = None
        self.current_cell = None
        self.max_hp = self.hp = hardness * self.MAX_HP

    def update(self):
        self.current_cell = self.game.game_field.get_cell_obj(self.game.game_field.get_cell((self.pos)))
        if isinstance(self.current_cell, Road):
            # Если текущее направление по оси X, то нас интересует только dx между мобом и клеткой
            if self.current_way in (LEFT, RIGHT):
                distance = self.get_x_center_distance(self.current_cell)
            else:
                distance = self.get_y_center_distance(self.current_cell)
            # Расстояние между центрами проверяется для того, чтобы моб поворачивал примерно по центру клетки
            if distance < 5:
                self.current_way = self.current_cell.way
        else:
            self.current_way = self.game.spawn_platform.get_way_to_road()

        dx, dy = Road.WAYS[self.current_way]
        self.rect.x = self.rect.x + dx * self.speed
        self.rect.y = self.rect.y + dy * self.speed

    def in_radius(self, weapon):
        return not any(d > weapon.radius for d in self - weapon)

    def hit(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.kill()

    def draw_hp_bar(self):
        hp_percent = (self.hp / self.max_hp)
        if round(hp_percent, 2) >= 0.67:
            color = GREEN
        elif 0.33 < round(hp_percent, 2) < 0.66:
            color = GOLDENROD
        else:
            color = RED
        fill = hp_percent * self.HP_BAR_LENGTH
        outline_rect = pg.Rect(self.rect.x, self.rect.y - 10, self.HP_BAR_LENGTH, self.HP_BAR_HEIGHT)
        fill_rect = pg.Rect(self.rect.x, self.rect.y - 10, fill, self.HP_BAR_HEIGHT)
        pg.draw.rect(self.game.surface, color, fill_rect)
        pg.draw.rect(self.game.surface, WHITE, outline_rect, 2)
