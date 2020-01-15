from core.objects.gameobject import GameObject


class Button(GameObject):
    IMAGE = None
    SPRITE_GROUPS = ["buttons"]

    def __init__(self, game, pos):
        super().__init__(game, pos=pos)

    def clicked(self, mouse_pos):
        return self.rect.collidepoint(*mouse_pos)

    def on_click(self):
        pass