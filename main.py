import pygame

from app.framework.bootstrap import *
from app import Game

pygame.init()

pygame.mouse.set_visible(False)

Game().run()
