from pynput import keyboard


# one key per input_action, can make it a list later
class InputAction:
    def __init__(self, key_name, function):
        self.key_name = key_name
        self.function = function

    def change_function(self, new_function):
        self.function = new_function

    def change_key(self, new_key_name):
        self.key_name = new_key_name


# standard function called by standard input_actions
def print_input_action(input_action_name):
    print(input_action_name)


# standard input_actions
input_actions = {
    "up": InputAction("w", print_input_action),
    "left": InputAction("a", print_input_action),
    "down": InputAction("s", print_input_action),
    "right": InputAction("d", print_input_action)
}


def on_press(key):
    try:
        for input_action_name, input_action in input_actions.items():
            if key.char == input_action.key_name:
                input_action.function(input_action_name)
    except AttributeError:
        pass


def on_release(key):
    pass


# create listener for the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
