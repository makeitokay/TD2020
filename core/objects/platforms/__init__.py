from .base import Base
from .platform import Platform
from .road import Road
from .spawn import Spawn
from .weapon import Weapon


def load_object(game, symbol, cell):
    if symbol == "w":
        return Weapon(game, cell)
    elif symbol == "s":
        return Spawn(game, cell)
    elif symbol == "b":
        return Base(game, cell)
    elif symbol in (">", "v", "<", "^"):
        return Road(game, cell, way=symbol)