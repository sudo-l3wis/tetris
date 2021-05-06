from . import Entity


class RenderableEntity(Entity):
    def __init__(self):
        super().__init__()
        self.__surface = None

    def set_surface(self, surface):
        self.__surface = surface

    def get_surface(self):
        return self.__surface

    def update(self, delta):
        pass

    def render(self, surface):
        surface.blit(self.get_surface(), self.get_pos())
