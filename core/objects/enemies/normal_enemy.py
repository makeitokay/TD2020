from core.objects.enemies.enemy import Enemy


class NormalEnemy(Enemy):
    IMAGE = "enemies/normal_enemy.png"

    SPRITE_GROUPS = ["enemies", "normal_enemies"]

    MAX_HP = 1

    def __init__(self, game, hardness, pos):
        super().__init__(game, hardness, pos=pos)
