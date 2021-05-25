from app.framework.singleton import Asset
from . import AbstractFacade


class SurfaceFacade(AbstractFacade):

    def __init__(self):
        super().__init__('surface')

    def invoke(self, key):
        _surface = config('sprites.{}'.format(key)).values()
        return asset('sprites').subsurface(tuple(_surface))
