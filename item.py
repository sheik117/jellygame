from jelly import Character


class Item:
    """
    Item class represents an item in the game
    """
    def __init__(self, name, sprite=None, stats=None, amount=1):
        """
        Constructor for Item class
        :param name: name of the item
        :type name: str
        :param sprite: sprite of the item
        :type sprite: Sprite
        :param stats: stats of the item
        :type stats: dict
        :param amount: amount of the item
        :type amount: int
        """
        self.name = name
        self.sprite = sprite
        self.stats = stats
        self.amount = amount;

    def add_stat(self, name, value):
        """
        Adds additional stat to the item
        :param name: name of the stat
        :type name: str
        :param value: value of the stat
        :type value: int
        """
        if self.stats is None:
            self.stats = {name: value}
        else:
            self.stats[name] = value

    def delete_item(self):
        """
        Deletes the item
        """
        del self

    def edit_item(self, name, sprite, stats):
        """
        Edits the item
        :param name: name of the item
        :type name: str
        :param sprite: sprite of the item
        :type sprite: Sprite
        :param stats: stats of the item
        :type stats: dict
        """
        self.name = name;
        self.sprite = sprite;
        self.stats = stats;

    # sets how many object instances of the item there are
    def set_amount(self, amount):
        """
        Sets the amount of the item
        :param amount: amount of the item
        :type amount: int
        """
        self.amount = amount;


class ConsumableItem(Item):
    """
    ConsumableItem class represents a consumable item in the game
    Extends Item class
    """
    def __init__(self, name, sprite, stats=None):
        """
        Constructor for ConsumableItem class
        :param name: name of the item
        :type name: str
        :param sprite: sprite of the item
        :type sprite: Sprite
        :param stats: stats of the item
        :type stats: dict
        """
        super().__init__(name, sprite, stats)

    def use_item(self, amount=None):
        """
        Uses the item
        :param amount: amount of the item to be used
        :type amount: int
        """
        if amount is None:
            amount = self.amount
        self.amount -= amount
        Character.add_stat(self.stats)
        if self.amount <= 0:
            self.delete_item()
