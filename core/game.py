import pygame as pg

from core.objects.dynamic_text import DynamicText
from core.utils import terminate, load_image, GOLD
from .settings import FPS, GAME_FIELD_WIDTH, CELL_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_FIELD_HEIGHT
from core.field.game_field import GameField

from core.objects.platforms.platform import Platform
from .objects.platforms.weapon_platform import WeaponPlatform

from core.field.weapon_shop_field import WeaponShopField


class Game:
    def __init__(self, surface, level=1):
        self.surface = surface
        self.clock = pg.time.Clock()

        self.sprite_groups = {
            "all": pg.sprite.Group(),
            "platforms": pg.sprite.Group(),
            "weapon_platforms": pg.sprite.Group(),
            "spawn": pg.sprite.Group(),
            "base": pg.sprite.Group(),
            "road": pg.sprite.Group(),
            "text": pg.sprite.Group(),

            "weapons": pg.sprite.Group(),
            "weapon_shop_objects": pg.sprite.Group(),
            "base_weapons": pg.sprite.Group(),

            "info": pg.sprite.Group()
        }

        self.game_field = GameField(self, (0, 0), level)
        self.game_field.init_level()

        self.coins = 200
        self.coin_image = load_image("coin.png")
        self.coin_counter = DynamicText(self, (100, 500), self.get_coins, color=GOLD, size=32)

        self.play_image = load_image("play.png")

        self.weapon_shop = WeaponShopField(self, (GAME_FIELD_WIDTH * CELL_SIZE, 100))
        self.weapon_shop.init_shop()

    def run(self):
        while True:
            self.events()
            self.update()
            self.clock.tick(FPS)

    def update(self):
        self.sprite_groups["all"].update()

        self.surface.fill((0, 0, 0))
        self.game_field.render()
        self.surface.blit(self.game_field, (0, 0))

        if isinstance(self.game_field.selected_cell_obj, Platform):
            self.surface.blit(self.game_field.selected_cell_obj.info_image, (GAME_FIELD_WIDTH * CELL_SIZE, 0))

        if isinstance(self.game_field.selected_cell_obj, WeaponPlatform):
            self.weapon_shop.render()
            self.surface.blit(self.weapon_shop, (GAME_FIELD_WIDTH * CELL_SIZE, 100))

        self.surface.blit(self.coin_image, (85, 580))
        self.surface.blit(self.coin_counter.image, (145, 580))

        self.surface.blit(self.play_image, (20, 580))

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouse_click_handler(event.pos)

    def mouse_click_handler(self, pos):
        self.weapon_shop.unselect_cell()
        if (cell := self.game_field.get_cell(pos)):
            self.game_field.on_click(cell)
        elif (cell := self.weapon_shop.get_cell(pos)):
            self.weapon_shop.on_click(cell)
        else:
            self.game_field.unselect_cell()

    def get_coins(self):
        return self.coins