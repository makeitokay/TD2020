import pygame as pg


class EventSpeedUpHandler:
    def __init__(self, speed):
        self.speed = speed

        self.start_time = pg.time.get_ticks()

        # Сколько времени мы ускорили за все разы, когда ускорение было активировано (сумма всех ускорений)
        self.speed_up_time = 0

        # Сколько мы ускорили времени начиная с того момента, как было активировано ускорение в последний раз
        self.current_speed_up_time = 0

    @property
    def speed_up(self):
        return self.speed_up_time + self.current_speed_up_time

    def update(self):
        if self.speed == 1:
            return
        self.current_speed_up_time = (self.speed - 1) * (pg.time.get_ticks() - self.start_time)

    def change_speed(self, speed):
        self.speed = speed
        self.speed_up_time += self.current_speed_up_time
        self.current_speed_up_time = 0
        self.start_time = pg.time.get_ticks()