from engine.jelly import Character


class Item:
    def __init__(self, name, sprite, stats=None, amount=1):
        self.name = name
        self.sprite = sprite
        self.stats = stats
        self.amount = amount;

    def add_stat(self, name, value):
        if self.stats is None:
            self.stats = {name: value}
        else:
            self.stats[name] = value

    def delete_item(self):
        del self

    def edit_item(self, name, sprite, stats):
        self.name = name;
        self.sprite = sprite;
        self.stats = stats;

    # sets how many object instances of the item there are
    def set_amount(self, amount):
        self.amount = amount;


class ConsumableItem(Item):
    def __init__(self, name, sprite, stats=None):
        super().__init__(name, sprite, stats)

    def use_item(self, amount=None):
        if amount is None:
            amount = self.amount
        self.amount -= amount
        Character.add_stat(self.stats)
        if self.amount <= 0:
            self.delete_item()
