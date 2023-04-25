import color as c


class Tile:
    """
    Tile class represents a square in the grid
    """
    def __init__(self, color=c.WHITE, sprite=None, jelly=None):
        """
        Constructor for Tile class
        :param color: background color of the tile
        :type color: color
        :param sprite: sprite of the tile
        :type sprite: sprite
        :param jelly: jelly on the tile
        :type jelly: jelly
        """
        self.color = color
        self.sprite = sprite
        self.jelly = jelly

    def get_color(self):
        """
        Returns the color of the tile
        :return: color
        :rtype: color
        """
        return self.color

    def set_color(self, color):
        """
        Sets the color of the tile
        :param color: color
        :type color: color
        """
        self.color = color

    def get_cord(self):
        """
        Returns the coordinates of the tile
        :return: coordinates
        :rtype: tuple
        """
        return self.cord


    def get_jelly(self):
        """
        Returns the jelly on the tile
        :return: jelly
        :rtype: jelly
        """
        return self.jelly

    def set_jelly(self, jelly):
        """
        Sets the jelly on the tile
        :param jelly: jelly
        :type jelly: jelly
        """
        self.jelly = jelly
    
    def get_terrain(self):
        """
        Returns the terrain type of the tile
        :return: terrain
        :rtype: terrain
        """
        pass

    def set_terrain(self, terrain):
        """
        Sets the terrain type of the tile
        :param terrain: terrain
        :type terrain: terrain
        """
        self.terrain = terrain


class Terrain:
    """
    Terrain class represents the terrain type of a tile
    """
    def __init__(self) -> None:
        """
        Constructor for Terrain class
        """
        pass


class Jelly():
    """
    Jelly class represents a generic game object
    """
    def __init__(self, color=c.WHITE, sprite=None, owner=0, inv=None, stats=None):
        """
        Constructor for Jelly class
        :param color: background color of the jelly
        :type color: color
        :param sprite: sprite of the jelly
        :type sprite: sprite
        :param owner: owner of the jelly
        :type owner: int
        :param inv: inventory of the jelly
        :type inv: Inventory
        :param stats: stats of the jelly
        :type stats: dict
        """
        self.color = color
        self.sprite = sprite
        self.inv = inv
        self.owner = owner
        self.stats = stats

    def set_sprite(self, sprite):
        """
        Sets the sprite of the jelly
        :param sprite: sprite
        :type sprite: sprite
        """
        self.sprite = sprite

    def get_color(self):
        """
        Returns the color of the jelly
        :return: color
        :rtype: color
        """
        return self.color

    def set_color(self, color):
        """
        Sets the color of the jelly
        :param color: color
        :type color: color
        """
        self.color = color

    def add_stat(self, name, value):
        """
        Adds additional stat to the jelly
        :param name: name of the stat
        :type name: str
        :param value: value of the stat
        :type value: int
        """
        if self.stats == None:
            self.stats = {name: value}
        else:
            self.stats[name] = value

    def set_pos(self, x, y):
        """
        Sets the position of the jelly
        :param x: x coordinate
        :type x: int
        :param y: y coordinate
        :type y: int
        """




class Character(Jelly):
    def __init__(self, hp=10, mp=10, color=c.WHITE, sprite=None, owner=0, inv=None, stats=None):
        """
        Constructor for Character class
        Extends Jelly class
        :param hp: health points
        :type hp: int
        :param mp: mana points
        :type mp: int
        :param color: background color of the character
        :type color: color
        :param sprite: sprite of the character
        :type sprite: str
        :param owner: faction the character belongs to
        :type owner: int
        :param inv: inventory of the character
        :type inv: dict
        :param stats: additional stats of the character
        :type stats: dict
        """
        super().__init__(color, sprite, owner, inv, stats)
        self.hp = hp
        self.max_hp = hp
        self.mp = mp
        self.max_mp = mp

    def movement(self, x, y):
        """
        Moves the character
        :param x: distance to move in the x direction
        :type x: int
        :param y: distance to move in the y direction 
        :type y: int
        """
        pass

class Player(Character):
    """
    A class representing a unique character controlled by the player
    """
    def input(self):
        pass