import pygame as pg

from .platform import Platform


class Spawn(Platform):
    IMAGE = "platforms/spawn.png"
    SPRITE_GROUPS = ["platforms", "spawn"]
    FRAMES_CHANGING = 35

    def __init__(self, game, cell):
        super().__init__(game, cell)

        self.angle = 1
        self.next_frame = pg.time.get_ticks()
        self.original_image = self.image

    def update(self, *args):
        if pg.time.get_ticks() > self.next_frame:
            center = self.rect.center
            self.image = pg.transform.rotate(self.original_image, self.angle % 360)
            self.angle += 1
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.next_frame += self.FRAMES_CHANGING
        super().update()