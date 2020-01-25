import pygame as pg

from .platform import Platform
from core.utils import load_waves, terminate
import core.objects.enemies

from core.events import NEXT_WAVE, ENEMY_SPAWN
from core.objects.platforms.road import Road


class Spawn(Platform):
    IMAGE = "platforms/spawn.png"
    INFO_IMAGE = "platforms_info/spawn.png"

    SPRITE_GROUPS = ["platforms", "spawn"]

    FRAMES_CHANGING = 90

    def __init__(self, game, cell):
        super().__init__(game, cell)

        self.angle = 1
        self.next_frame = pg.time.get_ticks()
        self.original_image = self.image

        self.level = None
        self.waves = None
        self.current_wave = 0
        self.current_enemy = 0

    def update(self, *args):
        if pg.time.get_ticks() > self.next_frame:
            center = self.rect.center
            self.image = pg.transform.rotate(self.original_image, self.angle % 360)
            self.angle += 1
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.next_frame += (self.FRAMES_CHANGING // self.speed)
        super().update()

    def set_level(self, level):
        self.level = level
        self.waves = load_waves(level)

    def next_wave(self):
        self.current_wave += 1
        self.current_enemy = 0

        wave_info = self.waves[self.current_wave - 1]

        if wave_info["time"] == -1:
            self.game.prepare_last_wave()

        self.game.set_event(ENEMY_SPAWN, wave_info["spawn_interval"])
        self.game.set_event(NEXT_WAVE, wave_info["time"])

        self.next_enemy()

    def next_enemy(self):
        wave_info = self.waves[self.current_wave - 1]
        for key in wave_info:
            if key in ("N",) and wave_info[key] > 0:
                core.objects.enemies.load_enemy(self.game, self.pos, key, int(wave_info["hardness"]))
                wave_info[key] -= 1

    def get_way_to_road(self):
        x, y = self.cell
        for i in range(-1, 2):
            for j in range(-1, 2):
                cell_obj = self.game.game_field.get_cell_obj((x + i, y + j))
                if isinstance(cell_obj, Road):
                    return cell_obj.way
