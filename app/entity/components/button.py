from . import Component
from app.types import ComponentType
#from app.events import ButtonClick


class Button(Component):

    def __init__(self, icon):
        super().__init__(ComponentType.UI)
        bounds = tuple(config('sprites.button').values())
        self.set_surface(asset('sprites').subsurface(bounds))
        self.icon = icon
        self.state = None

    def on_mount(self):
        self.state = ButtonState.DEFAULT

    def on_hover(self):
        self.state = ButtonState.HOVER

    def on_press(self):
        self.state = ButtonState.DEFAULT

    def on_move(self, pos):
        pass
