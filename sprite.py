from PIL import Image, ImageTk

class Sprite:
    """
    Sprite class for game objects
    """
    def __init__(self, file):
        """
        Constructor for Sprite class
        :param file: path to the image file
        :type file: str
        """
        self.image = Image.open(file)
        self.image = self.image.resize((32, 32))
        self.image = ImageTk.PhotoImage(self.image)
    
    # def __init__(self, file, size):
    #     self.image = Image.open(file)
    #     self.image = self.image.resize(size)
    #     self.image = ImageTk.PhotoImage(self.image)
    
    def getSize(self):
        """
        Returns the size of the sprite
        :return: size
        :rtype: tuple
        """
        return self.image.width(), self.image.height()
    
    def setSize(self, size):
        """
        Sets the size of the sprite
        :param size: size
        :type size: tuple
        """
        self.image = self.image.resize(size)
        self.image = ImageTk.PhotoImage(self.image)