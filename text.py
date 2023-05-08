from jellygame import color as c


class Text:
    def __init__(self, text, pos_x, pos_y, span_x, span_y, text_size, text_color=c.BLACK, background_color=c.WHITE):
        self.text = text
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.span_x = span_x
        self.span_y = span_y
        self.text_size = text_size
        self.text_color = text_color
        self.background_color = background_color

    def set_text(self, text):
        self.text = text

    def set_position(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def set_span(self, x, y):
        self.span_x = x
        self.span_y = y

    def set_text_size(self, size):
        self.text_size = size

    def set_text_color(self, color):
        self.text_color = color

    def set_background_color(self, color):
        self.background_color = color
