class Item:
    def __init__(self, name, sprite, stats=None):
        self.name = name
        self.sprite = sprite
        self.stats = stats

    def delete_item(self):
        pass

    def edit_item(self, name, sprite, stats):
        pass

    def set_amount(self, amount):
        pass

class UsableItem(Item):
    def __init__(self, name, sprite, stats=None):
        super().__init__(name, sprite, stats)

    def use_item(self, amount=None):
        pass

