import pygame as pg
from core.objects.gameobject import GameObject
import math


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

        self.target = None

        self.angle = 90

        self.original_image = self.image

    @property
    def _attack_speed(self):
        return (self.attack_speed * 1000) / self.speed

    @property
    def _target_angle(self):
        if not self.target:
            return None

        x, y = self.target.pos
        rel_x, rel_y = x - self.pos[0], y - self.pos[1]

        return (180 / math.pi) * -math.atan2(rel_y, rel_x)

    @property
    def _can_attack(self):
        return abs(self._target_angle - self.angle) < 15

    def update(self):
        self.do_rotate()

        if pg.time.get_ticks() >= self.next_attack + self._attack_speed:
            self.do_attack()

    def get_nearest_enemy_in_radius(self):
        distances = []
        for enemy in self.game.sprite_groups["enemies"].sprites():
            if not enemy.in_radius(self):
                continue
            distance = self.get_center_distance(enemy)
            distances.append((enemy, distance))
        if distances:
            return min(distances, key=lambda e: e[1])[0]

    def do_attack(self):
        self.set_target()

        if self.target and self._can_attack:
            self.target.hit(self.damage)
            self.next_attack = pg.time.get_ticks()

    def do_rotate(self):
        if not self.target:
            return

        # Поворачиваемся, если разница между требуемым и текущим углами большая (т. е. атаковать невозможно)
        if not self._can_attack:
            way_coefficient = 1 if self._target_angle > self.angle else -1
            self.angle += self.move_speed * self.speed * way_coefficient

            center = self.rect.center
            self.image = pg.transform.rotate(self.original_image, int(self.angle) - 90)
            self.rect = self.image.get_rect(center=center)

    def set_target(self):
        if self.target is None or not self.target.in_radius(self) or not self.target.alive():
            self.target = self.get_nearest_enemy_in_radius()
