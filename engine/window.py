import tkinter as tk
import jelly


class Window:
    def __init__(self, title):
        # create window
        self.window = tk.Tk()
        self.window.attributes("-fullscreen", True)
        self.window.title(title)
        self.tiles = [[jelly.Tile] for _ in range(0)]
        self.frames = tk.Frame()

    def create_grid(self, size_x, size_y):
        # render a grid of Tiles in the window
        self.tiles = [[jelly.Tile] * size_x for _ in range(size_y)]
        self.size_x = size_x
        self.size_y = size_y
        for y in range(size_y):
            self.window.rowconfigure([y], weight=1, minsize=38)
            self.window.columnconfigure([y], weight=1, minsize=38)
            for x in range(size_x):
                self.tiles[x][y] = jelly.Tile

    def draw_grid(self):
        # make Frame for every tile, or the jelly on top of it
        for y in range(self.size_y):
            for x in range(self.size_x):
                frame = tk.Frame(width=38, height=38)
                frame.grid(row=y, column=x)
                frame.configure(bg="#22aa11")

    def loop(self, function):
        # make function run as long as the window exists
        self.window.mainloop()

    def stop_loop(self, function):
        pass  # make function stop running

    def exit(self):
        pass  # close window and stop all loops
