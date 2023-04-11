from PIL import Image, ImageTk

class Sprite:
    def __init__(self, file):
        self.image = Image.open(file)
        self.image = self.image.resize((32, 32))
        self.image = ImageTk.PhotoImage(self.image)
    
    def __init__(self, file, size):
        self.image = Image.open(file)
        self.image = self.image.resize(size)
        self.image = ImageTk.PhotoImage(self.image)
    
    def getSize(self):
        return self.image.width(), self.image.height()
    
    def setSize(self, size):
        self.image = self.image.resize(size)
        self.image = ImageTk.PhotoImage(self.image)