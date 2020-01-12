from collections import namedtuple

event = namedtuple("event", "id delay")

ENEMY_SPAWN = event(29, 0)
NEXT_WAVE = event(30, 0)