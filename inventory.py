# Initializes inventory for a jelly entity
# Creates an array with the given size (length) which works as item slots for the jelly entity
class Inventory:
    """
    Inventory class represents the inventory of a jelly entity
    """
    def __init__(self, size=15):
        """
        Constructor for Inventory class
        :param size: size of the inventory
        :type size: int
        """
        self.items = []
        self.size = size

    def add_item(self, item):
        """
        Adds an item to the inventory
        :param item: item to be added
        :type item: Item
        """
        if self.items is None:
            self.items = [item]
        elif len(self.items) + item.amount > self.size:
            # inventory is full
            pass
        else:
            existing_item = next((x for x in self.items if x.name == item.name), None)
            if existing_item is not None:
                existing_item.amount += item.amount
            else:
                self.items.append(item)


    def remove_item(self, item, amount=0):
        """
        Removes an item from the inventory
        :param item: item to be removed
        :type item: Item
        :param amount: amount of the item to be removed (if < 1 default to item.amount)
        :type amount: int
        """
        # Removes item from inventory
        if amount < 1:
            amount = item.amount
        if self.items[item].name == item.name:
            if self.items[item].amount > amount:
                self.items[item].amount -= amount
            else:
                self.items.remove(item)
        else:
            # Item not in inventory
            pass


    def set_size(self, size):
        """
        Edits the size of the inventory
        :param size: new size of the inventory
        :type size: int
        """
        # Set size of inventory
        self.size = size

    def get_size(self):
        """
        Gets the size of the inventory
        :return: size of the inventory
        :rtype: int
        """
        return self.size
    
    def get_items(self):
        """
        Gets the items in the inventory
        :return: items in the inventory
        :rtype: list
        """
        return self.items
    
    def get_item(self, name):
        """
        Gets an item from the inventory
        :param name: name of the item
        :type name: str
        :return: item from the inventory
        :rtype: Item
        """
        return next((x for x in self.items if x.name == name), None)
   