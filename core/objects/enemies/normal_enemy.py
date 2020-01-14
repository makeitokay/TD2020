from core.objects.enemies.enemy import Enemy


class NormalEnemy(Enemy):
    IMAGE = "enemies/normal_enemy.png"

    SPRITE_GROUPS = ["enemies", "normal_enemies"]

    def __init__(self, game, pos):
        super().__init__(game, pos=pos)

        self.hp = 1