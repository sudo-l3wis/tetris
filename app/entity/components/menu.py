from . import Component


class MainMenu(Component):

    def __init__(self):
        super().__init__()
        bounds = tuple(config('sprites.box').values())
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
