import tkinter as tk
import jelly


class Window:
    def __init__(self, title):
        # create window
        self.window = tk.Tk()
        #self.window.attributes("-fullscreen", True)
        self.window.title(title)
        self.tiles = [[jelly.Tile] for _ in range(0)]

    def create_grid(self, size_x, size_y):
        # render a grid of Tiles in the window
        self.tiles = [[jelly.Tile] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        self.window.minsize(size_x*39, size_y*39)
        for y in range(size_y):
            for x in range(size_x):
                self.tiles[y][x] = jelly.Tile()

    def draw_grid(self):
        # make Frame for every tile, or the jelly on top of it
        for y in range(self.size_y):
            for x in range(self.size_x):
                self.draw_tile(x, y)

    def draw_tile(self, x, y):
        # draw tile
        frame = tk.Frame(self.window)
        frame.pack()
        frame.place(x=x*39, y=y*39, height=38, width=38)
        frame.configure(bg=self.tiles[y][x].get_color())

    def loop(self, function):
        # make function run as long as the window exists
        self.window.mainloop()

    def stop_loop(self, function):
        pass  # make function stop running

    def exit(self):
        pass  # close window and stop all loops
