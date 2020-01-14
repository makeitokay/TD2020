import pygame as pg
from core.objects.gameobject import GameObject
from core.utils import get_center_distance_from_way


class Weapon(GameObject):
    SPRITE_GROUPS = ["weapons"]

    IMAGE = None
    SHOP_IMAGE = None

    NAME = None

    def __init__(self, game, cell):
        super().__init__(game, game.game_field, cell)

        self.damage = 0
        self.radius = 0
        self.attack_speed = 0
        self.move_speed = 0

    def update(self):
        nearest_enemy = self.get_nearest_enemy_in_radius()
        if nearest_enemy:
            nearest_enemy.hit(self.damage)

    def get_nearest_enemy_in_radius(self):
        distances = []
        for enemy in self.game.sprite_groups["enemies"].sprites():
            if any(d > self.radius for d in self - enemy):
                continue
            distance = get_center_distance_from_way(self.rect, enemy.rect, enemy.current_way)
            distances.append((enemy, distance))
        if distances:
            return min(distances, key=lambda e: e[1])[0]
