from pygame import time

from . import RenderableEntity


class AnimatedEntity(RenderableEntity):
    def __init__(self):
        super().__init__()
        self.__frame = 0
        self.__frames = []
        self.__frame_rate = 0
        self.__frame_start = time.get_ticks()
        self.asset = 'sprites'
        self.absolute = False
        self.repeat = True
        self.animation_complete = False

    def get_frame(self):
        return self.__frame

    def set_frame(self, frame):
        self.__frame = frame

    def get_frames(self):
        return self.__frames

    def set_frames(self, frames):
        self.__frames = frames

    def get_frame_rate(self):
        return self.__frame_rate

    def set_frame_rate(self, frame_rate):
        self.__frame_rate = frame_rate

    def set_asset(self, asset):
        self.asset = asset
        if self.asset == 'sprites':
            self.absolute = False
        else:
            self.absolute = True

    def is_animation_complete(self):
        return self.animation_complete

    def update(self, delta):
        super().update(delta)
        current = time.get_ticks()

        if current - self.__frame_start >= self.__frame_rate:
            self.__frame_start = current
            if self.repeat:
                self.__frame = (self.__frame + 1) % len(self.__frames)
            elif self.__frame + 1 < len(self.__frames):
                self.__frame += 1
            else:
                self.animation_complete = True

    def get_surface(self):
        x, y = self.__frames[self.__frame]

        if not self.absolute:
            x *= self.get_width()
            y *= self.get_height()

        pos = (x, y, self.get_width(), self.get_height())

        return asset(self.asset).subsurface(pos)
