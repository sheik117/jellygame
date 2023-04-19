import pyaudio
from window import JellyWindow
import color as c
import jelly as j
import item as item
import audio as audio

gameWindow = JellyWindow("Jelly Game")

gameWindow.create_grid(20, 20)

player = j.Jelly(c.GREEN, "player")
gameWindow.tiles[5][5].set_jelly(player)
character = j.Character(player)
goblin = j.Jelly(c.RED, "goblin")
character = j.Character(goblin)
gameWindow.tiles[5][10].set_jelly(goblin)

sword = item.Item("Sword")
sword.add_stat("damage", 2)

gameWindow.draw_grid()

gameWindow.start()

