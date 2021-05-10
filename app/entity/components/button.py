from . import Component
from app.types import ComponentType
from app.types import ButtonState


class Button(Component):

    def __init__(self, icon):
        super().__init__(ComponentType.UI)
        self.icon = icon
        self.state = None

    def set(self, surface):
        conf = config('sprites.button')
        bounds = tuple(conf.values())
        self.set_surface(asset('sprites').subsurface(bounds))
        self.set_width(conf['width'])
        self.set_height(conf['height'])

    def on_mount(self):
        self.state = ButtonState.DEFAULT
        self.set('sprites.button')

    def on_hover(self):
        print(self.state)
        self.state = ButtonState.HOVER
        self.set('sprites.button_hover')

    def on_press(self):
        self.state = ButtonState.DEFAULT
        self.set('sprites.button')

    def on_move(self, pos):
        pass
