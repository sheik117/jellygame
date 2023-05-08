import tkinter as tk
import jelly as j
import text as t


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
        self.tiles = [[j.Tile] for _ in range(0)]
        self.texts = []

        self.canvas = tk.Canvas(self.tk_window)
        self.canvas.pack(fill=tk.BOTH, expand=True)


    def create_grid(self, size_x, size_y):
        """
        Creates a grid of Tiles
        :param size_x: number of tiles in x dimension
        :type size_x: int
        :param size_y: number of tiles in y dimension
        :type size_y: int
        """
        # render a grid of Tiles in the window
        self.tiles = [[j.Tile] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        for y in range(size_y):
            for x in range(size_x):
                self.tiles[y][x] = j.Tile()

    def add_text(self, text):
        self.texts.append(text)

    def draw_grid(self, offset_x=0, offset_y=0, tile_size=38, show_grid=True):
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
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.tile_size = tile_size
        self.show_grid = show_grid
        for widget in self.tk_window.winfo_children():
            widget.destroy()
        self.tk_window.minsize(self.size_x * (tile_size + show_grid), self.size_y * (tile_size + show_grid))
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.draw_tile(x, y)

        for i in range(len(self.texts)):
            self.draw_text(self.texts[i])


    # Draws canvas with grid
    def drawCanvas(self, offset_x=0, offset_y=0, tile_size=38):
        self.canvas.delete("all")
        for y in range(self.size_y):
            for x in range(self.size_x):
                tile = self.tiles[y][x]
                if tile.get_jelly() is not None:
                    tile = tile.get_jelly()
                self.canvas.create_rectangle(x * (tile_size + 1) + offset_x, y * (tile_size + 1) + offset_y,
                                             x * (tile_size + 1) + offset_x + tile_size,
                                             y * (tile_size + 1) + offset_y + tile_size, fill=tile.get_color())

    # sets tiles on the canvas
    def set_tiles_on_canvas(self, offset_x=0, offset_y=0, tile_size=38):
        for y in range(self.size_y):
            for x in range(self.size_x):
                tile = self.tiles[y][x]
                if tile.get_jelly() is not None:
                    tile = tile.get_jelly()
                self.canvas.create_rectangle(x * (tile_size + 1) + offset_x, y * (tile_size + 1) + offset_y,
                                             x * (tile_size + 1) + offset_x + tile_size,
                                             y * (tile_size + 1) + offset_y + tile_size, fill=tile.get_color())




    def draw_text(self, text):
        print(text.text)
        label = tk.Label(self.tk_window, text=text.text)
        label.pack()
        label.place(x=text.pos_x * (self.tile_size + self.show_grid) + self.offset_x,
                    y=text.pos_y * (self.tile_size + self.show_grid) + self.offset_y,
                    height=text.span_y * (self.tile_size + self.show_grid) - self.show_grid,
                    width=text.span_x * (self.tile_size + self.show_grid) - self.show_grid)
        label.configure(bg=text.background_color, fg=text.text_color, font=("Arial", text.text_size))

    def draw_tile(self, x, y):
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
        frame.place(x=x*(self.tile_size+self.show_grid)+self.offset_x,
                    y=y*(self.tile_size+self.show_grid)+self.offset_y,
                    height=self.tile_size,
                    width=self.tile_size)
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

    def get_canvas(self):
        return self.canvas
