import pygame as pg
import math

from core.objects.gameobject import GameObject


class Bullet(GameObject):
    SPRITE_GROUPS = ["bullets"]
    IMAGE = "bullets/bullet.png"

    def __init__(self, game, weapon, target):
        super().__init__(game, pos=weapon.gun_pos)

        self.target = target
        self.weapon = weapon

        self.move_speed = 30

    def update(self):
        way_x = 1 if self.target.rect.x > self.rect.x else -1
        way_y = 1 if self.target.rect.y > self.rect.y else -1

        delta_x = self.move_speed * self.speed * way_x
        delta_y = self.move_speed * self.speed * way_y
        if abs(delta_x) > abs(self.target.rect.x - self.rect.x):
            delta_x = self.target.rect.x - self.rect.x
        if abs(delta_y) > abs(self.target.rect.y - self.rect.y):
            delta_y = self.target.rect.y - self.rect.y

        self.rect.x += delta_x
        self.rect.y += delta_y

        if pg.sprite.collide_rect(self, self.target):
            self.target.hit(self.weapon.damage)
            self.kill()