from core.objects.gameobject import GameObject
from core.objects.platforms.road import Road
from core.utils import get_center_distance_from_way


class Enemy(GameObject):
    IMAGE = None

    SPRITE_GROUPS = ["enemies"]

    def __init__(self, game, pos):
        super().__init__(game, pos=pos)

        self.current_way = None

        self.hp = 0

    def update(self):
        self.current_cell = self.game.game_field.get_cell_obj(self.game.game_field.get_cell((self.pos)))
        if isinstance(self.current_cell, Road):
            if get_center_distance_from_way(self.rect, self.current_cell.rect, self.current_way) < 2:
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