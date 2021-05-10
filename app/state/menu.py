from . import State
from app.types import EntityType
from app.entity.components import Button

class MenuState(State):

    def start(self):
        w = config('display.width')
        h = config('display.height')

        bw = config('sprites.box.width')
        bh = config('sprites.box.height')

        self.pos = ((w - bw) / 2, (h - bh) / 2)

        bw = config('sprites.button.width')
        bh = config('sprites.button.height')

        btn_start = Button('play')
        btn_start.set_pos((w - bw) / 2, (h - bh) / 2)
        self.add_component(btn_start)

        super().start()

    def update(self, delta):
        super().update(delta)

    def render(self, surface):
        super().render(surface)
        draw(surface, 'sprites.box', self.pos)
