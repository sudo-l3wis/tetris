import pygame
import sys

from pygame.locals import *
from app.state import MenuState


class Game:

    def __init__(self, manager):
        self.manager = manager
        pygame.display.set_caption("Tetris")
        width = config('display.width')
        height = config('display.height')
        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.last_frame = pygame.time.get_ticks()
        self.fps = 60
        self.running = True

    def run(self):
        self.manager.start()
        while self.running:
            self.events()
            self.update()
            self.render()

    def events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                self.manager.on_key(event.key)

    def update(self):
        t = pygame.time.get_ticks()
        delta = (t - self.last_frame) / 1000.0
        self.last_frame = t
        self.manager.update(delta)

    def render(self,):
        self.surface.fill((0, 0, 0))
        self.manager.render(self.surface)
        pygame.display.update()
        self.clock.tick(self.fps)
