from . import Component
from app.types import ButtonState


class Button(Component):

    def __init__(self, icon):
        super().__init__()
        self.icon = icon
        self.handler = None
        self.state = None
        self.is_pressed = False
        self.icon = surface('icon_{}'.format(icon))
        self.set_width(config('sprites.button.width'))
        self.set_height(config('sprites.button.height'))

    def handle(self, handler):
        self.handler = handler

    def render(self, surface):
        if self.state is ButtonState.DEFAULT:
            draw(surface, 'sprites.button', self.get_pos())
        elif self.state is ButtonState.HOVER:
            draw(surface, 'sprites.button_hover', self.get_pos())
        elif self.state is ButtonState.PRESSED:
            draw(surface, 'sprites.button_pressed', self.get_pos())

        w, h = self.icon.get_size()

        offset_x = (self.get_width() - w) / 2
        offset_y = (self.get_height() - h) / 2

        pos = (offset_x + self.get_x(), offset_y + self.get_y())

        surface.blit(self.icon, pos)


    def update(self, delta):
        super().update(delta)
        if self.state is not ButtonState.PRESSED:
            if self.is_pressed:
                self.is_pressed = False
                if self.handler:
                    self.handler()

    def on_mount(self):
        self.state = ButtonState.DEFAULT

    def on_hover(self):
        self.state = ButtonState.HOVER

    def on_leave(self):
        self.state = ButtonState.DEFAULT

    def on_press(self):
        self.state = ButtonState.PRESSED
        self.is_pressed = True

    def on_move(self, pos):
        pass
