import pygame

from app.framework.bootstrap import *
from app import Game
from app.framework.singleton import StateManager

pygame.init()

pygame.mouse.set_visible(False)

Game(StateManager()).run()
