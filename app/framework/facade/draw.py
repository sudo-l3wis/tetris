from app.framework.singleton import Asset
from . import AbstractFacade


class DrawFacade(AbstractFacade):

    def __init__(self):
        super().__init__('draw')

    def invoke(self, surface, entity, pos=None):
        bounds = config(entity)

        image = asset('sprites').subsurface(
            (bounds['x'], bounds['y'], bounds['width'], bounds['height'])
        )

        # If a position isn't provided draw at the center.
        if pos is None:
            width = config('display.width')
            height = config('display.height')

            cx = (width - bounds['width']) / 2
            cy = (height - bounds['height']) / 2

            pos = (cx, cy)

        surface.blit(image, pos)
