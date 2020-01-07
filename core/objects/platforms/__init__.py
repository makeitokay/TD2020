from .base import Base
from .platform import Platform
from .road import Road
from .spawn import Spawn
from core.objects.platforms.weapon_platform import WeaponPlatform


def load_object(game, symbol, cell):
    if symbol == "w":
        return WeaponPlatform(game, cell)
    elif symbol == "s":
        return Spawn(game, cell)
    elif symbol == "b":
        return Base(game, cell)
    elif symbol in (">", "v", "<", "^"):
        return Road(game, cell, way=symbol)
    else:
        return Platform(game, cell)