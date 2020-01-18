import pygame as pg


class Event:
    def __init__(self, game, id, delay):
        self.game = game
        self.id = id
        self.delay = delay

        self.speed = self.game.speed

        self.start_time = pg.time.get_ticks()

        self.ticks = None
        self.cycles = 0

    @property
    def time_to_trigger(self):
        return int(((self.cycles + 1) * self.delay - pg.time.get_ticks() + self.start_time) / self.speed)

    def trigger(self):
        self.ticks = pg.time.get_ticks()
        self.cycles += 1

    def change_speed(self, speed):
        if speed > self.speed:
            pg.time.set_timer(self.id, int(self.time_to_trigger / (speed / self.speed)))
        else:
            pg.time.set_timer(self.id, int(self.time_to_trigger * (speed / self.speed)))

        self.speed = speed