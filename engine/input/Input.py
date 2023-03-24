from pynput import keyboard


class InputAction:
    def __init__(self, input, function):
        self.input = input
        self.function = function


def print_input_action(input_action_name):
    print(input_action_name)


# standard inputs
input_actions = {
    "up": InputAction("w", print_input_action)
}


def on_press(key):
    try:
        for input_action_name, input_action in input_actions.items():
            if key.char == input_action.input:
                input_action.function(input_action_name)
    except AttributeError:
        pass


def on_release(key):
    pass


# create listener for the keyboard
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
