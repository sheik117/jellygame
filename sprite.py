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


    def renderSprite(self):
        """
        Returns the sprite
        :return: sprite
        :rtype: PhotoImage
        """
        return self.photo_image

    def drawSprite(self, canvas, x, y):
        """
        Creates the sprite on the canvas
        :param canvas: canvas to create the sprite on
        :type canvas: Canvas
        :param x: x coordinate of the sprite
        :type x: int
        :param y: y coordinate of the sprite
        :type y: int
        """
        self.sprite = canvas.create_image(x, y, image=self.photo_image)