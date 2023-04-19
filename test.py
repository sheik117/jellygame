import pyaudio
import engine
from engine.jelly_window import JellyWindow
import engine.color as c
import engine.jelly as j
import engine.item as item
import engine.audio as audio

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

