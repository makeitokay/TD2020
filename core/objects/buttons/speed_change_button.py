from core.objects.buttons.button import Button
from core.utils import load_image


class SpeedChangeButton(Button):
    IMAGE = "buttons/speed_change_buttons/1x.png"

    STATE_IMAGES = {
        1: "buttons/speed_change_buttons/1x.png",
        2: "buttons/speed_change_buttons/2x.png",
        3: "buttons/speed_change_buttons/3x.png"
    }

    def __init__(self, game, pos):
        super().__init__(game, pos)

        self.state = 1

        self.state_images = {number: load_image(image) for number, image in self.STATE_IMAGES.items()}

    def on_click(self):
        self.state = self.state % len(self.STATE_IMAGES) + 1
        self.image = self.state_images[self.state]
        self.game.change_speed(self.state)