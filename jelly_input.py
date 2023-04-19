import tkinter as tk


# one key per input_action, can make it a list later
class InputAction:
    def __init__(self, window, key_string, function):
        self.window = window.window
        self.key_string = key_string
        self.function = function
        self.func_id = self.window.bind(key_string, function)

    def change_function(self, new_function):
        self.function = new_function
        self.window.unbind(self.key_string, self.func_id)
        self.func_id = self.window.bind(self.key_string, new_function)

    def change_key(self, new_key_string):
        self.key_string = new_key_string
        self.window.unbind(self.key_string, self.func_id)
        self.func_id = self.window.bind(self.key_string, self.function)


# standard function called by standard input_actions
def print_input_action(input_action_name):
    print(input_action_name)


# standard input_actions
input_actions = {
    #"up": InputAction(w, "<w>", print_input_action),
    #"left": InputAction(w, "<a>", print_input_action),
    #"down": InputAction(w, "<s>", print_input_action),
    #"right": InputAction(w, "<d>", print_input_action)
}
