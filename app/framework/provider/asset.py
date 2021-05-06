import pygame
import os

from app.framework.singleton import Asset
from . import AbstractProvider


class AssetProvider(AbstractProvider):

    def __init__(self):
        self.assets = {
            'sprites': 'sprites.png'
        }

    def register(self):
        """Load game assets."""
        assets = {}
        for name, path in self.assets.items():
            asset_path = os.path.abspath('assets/{}'.format(path))
            assets[name] = pygame.image.load(asset_path)

        Asset().set_assets(assets)
