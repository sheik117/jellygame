import color
import window as jw
import jelly
import input as i
import audio
import text as t


def print_hp(event=None):
    print("test")
    i.input_actions.get("test").change_key("<y>")
    print(player.hp)


ouf = audio.Audio("ouf.wav")
x = 1
y = 1
def move_up(event):
    global y
    y -= z
    w.draw_grid(x, y, z)
    ouf.play()
    player.hp -= 1
def move_left(event):
    global x
    x -= z
    w.draw_grid(x, y, z)
    ouf.play()
    player.hp -= 1
def move_right(event):
    global x
    x += z
    w.draw_grid(x, y, z)
    ouf.play()
    player.hp -= 1
def move_down(event):
    global y
    y += z
    w.draw_grid(x, y, z)
    ouf.play()
    player.hp -= 1

z = 38
def zoom(event):
    global z
    if event.char == "i":
        z += 4
        w.draw_grid(x, y, z)
    else:
        z -= 4
        w.draw_grid(x, y, z)


w = jw.Window("Jelly")
w.create_grid(20, 10)
#w.tiles[2][4].set_color("#000000")
player = jelly.Player(10, 10, "#ff0000")
w.tiles[2][4].set_jelly(player)
w.draw_grid()
w.tk_window.after(10000, print_hp)
w.draw_grid()

action = i.InputAction(w, "<t>", print_hp)
i.input_actions.update({"test": action})

i.input_actions.update({"up": i.InputAction(w, "<w>", move_up)})
i.input_actions.update({"left": i.InputAction(w, "<a>", move_left)})
i.input_actions.update({"right": i.InputAction(w, "<d>", move_right)})
i.input_actions.update({"down": i.InputAction(w, "<s>", move_down)})
i.input_actions.update({"zoom_in": i.InputAction(w, "<i>", zoom)})
i.input_actions.update({"zoom_out": i.InputAction(w, "<o>", zoom)})
i.input_actions["zoom_out"] = i.InputAction(w, "<o>", zoom)

#t = w.window.bind('<t>', test)
#w.window.unbind('<t>', t)
#w.window.bind('<Up>', move_player)

txt = t.Text("player here ->", 1, 2, 3, 1, 12, color.RED, color.YELLOW)
w.add_text(txt)
w.draw_grid(0, 0, 38)

w.start()
