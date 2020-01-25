from core.objects.enemies.normal_enemy import NormalEnemy
from random import randint


def load_enemy(game, spawn_platform_pos, symbol, hardness=1):
    spawn_x, spawn_y = spawn_platform_pos
    enemy_pos =  spawn_x + randint(-2, 2), spawn_y + 15 + randint(-2, 2)
    if symbol == "N":
        return NormalEnemy(game, hardness, enemy_pos)