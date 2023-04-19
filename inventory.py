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
        self.size = size

    def add_item(self, item):
        """
        Adds an item to the inventory
        :param item: item to be added
        :type item: Item
        """
        pass # Adds item to inventory

    def remove_item(self, item):
        """
        Removes an item from the inventory
        :param item: item to be removed
        :type item: Item
        """
        pass # Removes item from inventory

    def edit_size(self, size):
        """
        Edits the size of the inventory
        :param size: new size of the inventory
        :type size: int
        """
        pass # Edit size of inventory