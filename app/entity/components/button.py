from . import Component
from app.types import ButtonState


class Button(Component):

    def __init__(self):
        super().__init__()
        self.handler = None
        self.state = None
        self.is_pressed = False

    def set(self, surface):
        conf = config(surface)
        bounds = tuple(conf.values())
        self.set_surface(asset('sprites').subsurface(bounds))
        self.set_width(conf['width'])
        self.set_height(conf['height'])

    def handle(self, handler):
        self.handler = handler

    def update(self, delta):
        super().update(delta)
        if self.state is not ButtonState.PRESSED:
            if self.is_pressed:
                self.is_pressed = False
                if self.handler:
                    self.handler()

    def on_mount(self):
        self.state = ButtonState.DEFAULT
        self.set('sprites.button')

    def on_hover(self):
        self.state = ButtonState.HOVER
        self.set('sprites.button_hover')

    def on_leave(self):
        self.state = ButtonState.DEFAULT
        self.set('sprites.button')

    def on_press(self):
        self.state = ButtonState.PRESSED
        self.set('sprites.button_pressed')
        self.is_pressed = True

    def on_move(self, pos):
        pass
