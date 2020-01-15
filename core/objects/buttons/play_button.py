from core.objects.buttons.button import Button


class PlayButton(Button):
    IMAGE = "buttons/play.png"

    def __init__(self, game, pos):
        super().__init__(game, pos)

    def on_click(self):
        self.game.start_game()
        self.kill()