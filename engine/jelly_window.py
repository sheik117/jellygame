import tkinter as tk
import jelly


class JellyWindow:
    def __init__(self, title, tile_size=38):
        # create window
        self.window = tk.Tk()
        #self.window.attributes("-fullscreen", True)
        self.window.title(title)
        self.tiles = [[jelly.Tile] for _ in range(0)]
        self.tile_size = tile_size

    def create_grid(self, size_x, size_y):
        # render a grid of Tiles in the window
        self.tiles = [[jelly.Tile] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        self.window.minsize(size_x*(self.tile_size+1), size_y*(self.tile_size+1))
        for y in range(size_y):
            for x in range(size_x):
                self.tiles[y][x] = jelly.Tile()

    def draw_grid(self, offset_x=0, offset_y=0):
        # make Frame for every tile, or the jelly on top of it
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.draw_tile(x, y, offset_x, offset_y)

    def draw_tile(self, x, y, offset_x=0, offset_y=0):
        # draw tile
        tile = self.tiles[y][x]
        if tile.get_jelly() is not None:
            print("has jelly")
            tile = tile.get_jelly()
        frame = tk.Frame(self.window)
        frame.pack()
        frame.place(x=x*(self.tile_size+1)+offset_x*self.tile_size, y=y*(self.tile_size+1)+offset_y*self.tile_size, height=self.tile_size, width=self.tile_size)
        frame.configure(bg=tile.get_color())

    def loop(self, function):
        # make function run as long as the window exists
        pass

    def stop_loop(self, function):
        pass  # make function stop running

    def start(self):
        self.window.mainloop()

    def exit(self):
        pass  # close window and stop all loops
