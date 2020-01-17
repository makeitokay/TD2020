import pygame as pg

from core.objects.dynamic_text import DynamicText
from core.utils import terminate, load_image, GOLD, WHITE, RED
from .settings import FPS, SPRITE_GROUPS, RIGHT_BLOCK_X
from core.field.game_field import GameField

from core.objects.platforms.platform import Platform
from .objects.platforms.weapon_platform import WeaponPlatform

from core.field.weapon_shop_field import WeaponShopField
from core.events import ENEMY_SPAWN, NEXT_WAVE
from core.objects.buttons.play_button import PlayButton
from core.objects.buttons.speed_change_button import SpeedChangeButton


class Game:
    def __init__(self, surface, level=1):
        self.surface = surface
        self.level = level
        self.clock = pg.time.Clock()

        self.game_started = False

        self.sprite_groups = {
            group: pg.sprite.Group() for group in SPRITE_GROUPS
        }

        self.hp = 20

        self.game_field = GameField(self, (0, 0), level)
        self.game_field.init_level()
        self.spawn_platform = self.game_field.get_spawn_platform()

        self.coins = 200
        self.coin_image = load_image("coin.png")
        self.coin_counter = DynamicText(self, (145, 580), self.get_coins, color=GOLD, size=32)

        self.play_image_button = PlayButton(self, (20, 580))
        self.speed_change_button = None

        self.wave_image = load_image("wave.png")
        self.wave_counter = DynamicText(self, (285, 580), self.get_current_wave, color=WHITE, size=32)

        self.life_image = load_image("life.png")
        self.life_counter = DynamicText(self, (355, 580), self.get_current_hp, color=RED, size=32)

        self.weapon_shop = WeaponShopField(self, (RIGHT_BLOCK_X, 100))
        self.weapon_shop.init_shop()
        self.click_to_confirm_image = load_image("click_to_confirm.png")

    @property
    def weapon_shop_opened(self):
        return isinstance(self.game_field.selected_cell_obj, WeaponPlatform)

    def start_game(self):
        self.spawn_platform.next_wave()
        self.game_started = True

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
            self.surface.blit(self.game_field.selected_cell_obj.info_image, (RIGHT_BLOCK_X, 0))

        if self.weapon_shop_opened:
            self.weapon_shop.render()
            self.surface.blit(self.weapon_shop, (RIGHT_BLOCK_X, 100))
            if self.weapon_shop.selected_cell_obj is not None:
                self.surface.blit(self.click_to_confirm_image, (RIGHT_BLOCK_X, 310))

        self.surface.blit(self.coin_image, (85, 580))
        self.surface.blit(self.coin_counter.image, self.coin_counter.pos)

        self.surface.blit(self.wave_image, (210, 570))
        self.surface.blit(self.wave_counter.image, self.wave_counter.pos)

        self.surface.blit(self.life_image, (305, 580))
        self.surface.blit(self.life_counter.image, self.life_counter.pos)

        self.sprite_groups["enemies"].draw(self.surface)
        self.sprite_groups["buttons"].draw(self.surface)

        for enemy in self.sprite_groups["enemies"].sprites():
            enemy.draw_hp_bar()

        pg.display.update()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                terminate()
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouse_click_handler(event.pos)
            elif event.type == ENEMY_SPAWN.id:
                self.spawn_platform.next_enemy()
            elif event.type == NEXT_WAVE.id:
                self.spawn_platform.next_wave()

    def mouse_click_handler(self, pos):
        if cell := self.game_field.get_cell(pos):
            self.game_field.on_click(cell)
        elif (cell := self.weapon_shop.get_cell(pos)) and self.weapon_shop_opened:
            self.weapon_shop.on_click(cell)
        else:
            self.game_field.unselect_cell()

        for button in self.sprite_groups["buttons"].sprites():
            if button.alive() and button.clicked(pos):
                button.on_click()
                break

    def get_coins(self):
        return self.coins

    def get_current_wave(self):
        return self.spawn_platform.current_wave

    def get_current_hp(self):
        return self.hp

    def buy_weapon(self, weapon_class):
        if self.coins < weapon_class.COST:
            return

        self.coins -= weapon_class.COST
        self.game_field.set_weapon(weapon_class)

    def set_event(self, id, delay):
        pg.time.set_timer(id, delay)

    def init_speed_change_button(self):
        self.speed_change_button = SpeedChangeButton(self, (20, 580))

    def change_speed(self, speed):
        for sprite in self.sprite_groups["all"].sprites():
            sprite.change_speed(speed)