from . import Component
from app.types import ComponentType


class Mouse(Component):

    def __init__(self):
        super().__init__(ComponentType.UI)
        bounds = tuple(config('sprites.mouse').values())
        self.set_surface(asset('sprites').subsurface(bounds))
        self.state = None

    def on_mount(self):
        pass

    def on_hover(self):
        pass

    def on_press(self):
        pass

    def on_click(self):
        pass

    def on_move(self, pos):
        self.set_pos(*pos)
