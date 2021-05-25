import pygame

from . import Component


class Label(Component):

    def __init__(self, text):
        super().__init__()
        self.set_text(text)

    def set_text(self, text):
        w = sum([config('sprites.text.{}'.format(i))['width'] for i in text]) + 2 * (len(text) - 1)
        h = max([config('sprites.text.{}'.format(i))['height'] for i in text])
        self.set_width(w)
        self.set_height(h)
        txt_surface = pygame.Surface((w, h), flags=pygame.SRCALPHA)

        x, y = 0, 0
        for character in text:
            _surface = surface('text.{}'.format(character))
            txt_surface.blit(_surface, (x, y))
            w, h = _surface.get_size()
            x += w + 2

        self.set_surface(txt_surface)

    def on_mount(self):
        pass

    def on_hover(self):
        pass

    def on_leave(self):
        pass

    def on_press(self):
        pass

    def on_click(self):
        pass

    def on_move(self, pos):
        pass
