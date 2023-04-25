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
player.sprite = sprite
sprite.createImage(gameWindow)

sword = jg.item.Item("Sword")
sword.add_stat("damage", 2)

gameWindow.draw_grid()

gameWindow.start()

