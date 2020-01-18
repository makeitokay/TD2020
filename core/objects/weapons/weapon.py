import pygame as pg
from core.objects.gameobject import GameObject


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

        self.next_attack = pg.time.get_ticks()

    @property
    def _attack_speed(self):
        return (self.attack_speed * 1000) / self.speed

    def update(self):
        if pg.time.get_ticks() < self.next_attack:
            return

        nearest_enemy = self.get_nearest_enemy_in_radius()
        if nearest_enemy:
            nearest_enemy.hit(self.damage)

        self.next_attack += self._attack_speed

    def get_nearest_enemy_in_radius(self):
        distances = []
        for enemy in self.game.sprite_groups["enemies"].sprites():
            if any(d > self.radius for d in self - enemy):
                continue
            distance = self.get_center_distance(enemy)
            distances.append((enemy, distance))
        if distances:
            return min(distances, key=lambda e: e[1])[0]
