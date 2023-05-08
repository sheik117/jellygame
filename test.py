import jellygame as jg

gameWindow = jg.window.Window("Jelly Game")

gameWindow.create_grid(20, 20)

player = jg.jelly.Jelly(jg.color.GREEN, "player")
gameWindow.tiles[5][5].set_jelly(player)
character = jg.jelly.Character(player)
goblin = jg.jelly.Jelly(jg.color.RED, "goblin")
character = jg.jelly.Character(goblin)
gameWindow.tiles[5][10].set_jelly(goblin)

sprite = jg.sprite.Sprite("player.png")

gameWindow.drawCanvas()
player.set_sprite(sprite)
#sprite.drawSprite(gameWindow.get_canvas(), 5, 5)
#player.get_sprite().drawSprite(gameWindow.get_canvas(), 5, 5)
tile = gameWindow.tiles[5][5]
jelly = tile.get_jelly()
sprite = jelly.get_sprite()
sprite.drawSprite(gameWindow.get_canvas(), 5, 5)
#gameWindow.tiles[5][5].get_jelly().get_sprite().drawSprite(gameWindow.get_canvas(), [5, 5])

#gameWindow.draw_grid()


sword = jg.item.Item("Sword")
sword.add_stat("damage", 2)
gameWindow.start()

