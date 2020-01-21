import pygame as pg

from core.events.event_speedup_handler import EventSpeedUpHandler

class Event:
    def __init__(self, game, id, delay):
        self.game = game
        self.id = id
        self.delay = delay

        self.speed_up_handler = EventSpeedUpHandler(self.game.speed)

        self.speed = self.game.speed

        self.start_time = pg.time.get_ticks()

        self.ticks = None
        self.cycles = 0

        self.once = False

        pg.time.set_timer(self.id, int(self.delay / self.speed))

    @property
    def time_to_trigger(self):
        """
        Время до срабатывания ивента - секунды ускорены в соответствии с текущей скоростью
        """
        self.speed_up_handler.update()
        speed_up_time = self.speed_up_handler.speed_up
        ticks = pg.time.get_ticks()
        return (self.cycles + 1) * self.delay - ticks + self.start_time - speed_up_time

    def trigger(self):
        self.ticks = pg.time.get_ticks()
        self.cycles += 1

        if self.once:
            pg.time.set_timer(self.id, int(self.delay / self.speed))
            self.once = False

    def change_speed(self, speed):
        if speed > self.speed:
            pg.time.set_timer(self.id, int(self.time_to_trigger / speed))
        else:
            pg.time.set_timer(self.id, int(self.time_to_trigger * speed))

        self.speed = speed
        self.once = True
        self.speed_up_handler.change_speed(speed)
