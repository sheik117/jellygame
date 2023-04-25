from PIL import Image, ImageTk
import tkinter as tk

class Sprite:
    """
    Sprite class for game objects
    """
    def __init__(self, file, size=(32, 32)):
        """
        Constructor for Sprite class
        :param file: path to the image file
        :type file: str
        :param size: size of the sprite, default is (32, 32)
        :type size: tuple
        """
        self.image = Image.open(file)
        self.image = self.image.resize(size)
        self.photo_image = ImageTk.PhotoImage(self.image)
    
    def getSize(self):
        """
        Returns the size of the sprite
        :return: size
        :rtype: tuple
        """
        return self.photo_image.width(), self.photo_image.height()
    
    def setSize(self, size):
        """
        Sets the size of the sprite
        :param size: size
        :type size: tuple
        """
        self.photo_image.config(width=size[0], height=size[1])

    def getImage(self):
        """
        Returns the image of the sprite
        :return: image
        :rtype: Image
        """
        return self.image


    def createImage(self, gameWindow):
        # create a Canvas object
        canvas = tk.Canvas(gameWindow, width=500, height=500)
        canvas.pack()

        # create a Sprite object
        sprite = Sprite('player.png')

        # add the sprite to the canvas
        canvas.create_image(100, 100, image=sprite.photo_image)
