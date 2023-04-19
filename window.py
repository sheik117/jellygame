import tkinter as tk
import jelly


class Window:
    def __init__(self, title):
        """
        Constructor for Window class

        :param title: Title of the window
        :type title: str
        """
        self.tk_window = tk.Tk()
        #self.window.attributes("-fullscreen", True)
        self.tk_window.title(title)
        self.tiles = [[jelly.Tile] for _ in range(0)]

    def create_grid(self, size_x, size_y):
        """
        Creates a grid of Tiles
        :param size_x: number of tiles in x dimension
        :type size_x: int
        :param size_y: number of tiles in y dimension
        :type size_y: int
        """
        # render a grid of Tiles in the window
        self.tiles = [[jelly.Tile] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        for y in range(size_y):
            for x in range(size_x):
                self.tiles[y][x] = jelly.Tile()

    def draw_grid(self, offset_x=0, offset_y=0, tile_size=38):
        """
        Draws (renders) the grid of Tiles
        :param offset_x: offset in x dimension
        :type offset_x: int
        :param offset_y: offset in y dimension
        :type offset_y: int
        :param tile_size: size of the tiles
        :type tile_size: int
        """
        # make Frame for every tile, or the jelly on top of it
        for widget in self.tk_window.winfo_children():
            widget.destroy()
        self.tk_window.minsize(self.size_x * (tile_size + 1), self.size_y * (tile_size + 1))
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.draw_tile(x, y, offset_x, offset_y, tile_size)

    def draw_tile(self, x, y, offset_x=0, offset_y=0, tile_size=38):
        """
        Draws (renders) a single tile
        :param x: x coordinate of the tile
        :type x: int
        :param y: y coordinate of the tile
        :type y: int
        :param offset_x: offset in x dimension
        :type offset_x: int
        :param offset_y: offset in y dimension
        :type offset_y: int
        :param tile_size: size of the tiles
        :type tile_size: int
        """
        # draw tile
        tile = self.tiles[y][x]
        if tile.get_jelly() is not None:
            tile = tile.get_jelly()
        frame = tk.Frame(self.tk_window)
        frame.pack()
        frame.place(x=x*(tile_size+1)+offset_x, y=y*(tile_size+1)+offset_y, height=tile_size, width=tile_size)
        frame.configure(bg=tile.get_color())

    def loop(self, function):
        # make function run as long as the window exists
        pass

    def stop_loop(self, function):
        pass  # make function stop running

    def start(self):
        self.tk_window.mainloop()

    def exit(self):
        pass  # close window and stop all loops
