import color as c


class Tile:
    def __init__(self, color=c.WHITE, sprite=None, jelly=None):
        self.color = color
        self.sprite = sprite
        self.jelly = jelly

    def get_cord(self):
        pass

    def get_jelly(self):
        pass

    def set_jelly(self, jelly):
        self.jelly = jelly
    
    def get_terrain(self):
        pass

    def set_terrain(self, terrain):
        self.terrain = terrain

class Terrain:
    def __init__(self) -> None:
        pass


class Jelly():
    def __init__(self, color=c.WHITE, sprite=None, owner=0, jelly=None):
        super().__init__(self, color, sprite, jelly)
        self.owner = owner

    def movement(x, y):
        pass


class Player(Jelly):
    def input(self):
        pass