from core.objects.gameobject import GameObject
from core.objects.platforms.road import Road

class Enemy(GameObject):
    IMAGE = None

    SPRITE_GROUPS = ["enemies"]

    def __init__(self, game, pos):
        super().__init__(game, pos=pos)

    def update(self):
        self.current_cell = self.game.game_field.get_cell_obj(self.game.game_field.get_cell(self.pos))
        if isinstance(self.current_cell, Road):
            way = self.current_cell.way
        else:
            way = self.game.spawn_platform.get_way_to_road()

        dx, dy = Road.WAYS[way]
        self.rect.x += dx
        self.rect.y += dy
