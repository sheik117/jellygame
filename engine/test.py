import pyaudio
import engine as jg
from engine.jelly_window import JellyWindow
import engine.color as c

gameWindow = JellyWindow("Jelly Game")

gameWindow.create_grid(20, 20)

gameWindow.tiles[5][5].set_color(c.GREEN)
gameWindow.tiles[5][8].set_color(c.RED)

gameWindow.draw_grid()

gameWindow.start()

