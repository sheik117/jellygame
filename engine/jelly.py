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
    def __init__(self, color=c.WHITE, sprite=None, owner=0, jelly=None, inv=None, stats=None):
        #super().__init__(self, color, sprite, jelly)
        self.color = color
        self.sprite = sprite
        self.jelly = jelly
        self.inv = inv
        self.owner = owner
        self.stats = stats

    def add_stat(self, name, value):
        if self.stats == None:
            self.stats = {name : value}
        else:
            self.stats[name] = value


class Character(Jelly):
    def __init__(self, hp=10, mp=10, color=c.WHITE, sprite=None, owner=0, jelly=None, inv=None, stats=None):
        super().__init__(color, sprite, owner, jelly, inv, stats)
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp



    def movement(x, y):
        pass

class Player(Jelly):
    def input(self):
        pass