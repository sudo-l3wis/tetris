from app.framework.singleton import Asset
from . import AbstractFacade


class AssetFacade(AbstractFacade):

    def __init__(self):
        super().__init__('asset')

    def invoke(self, key=False):
        if key:
            return Asset().get_asset(key)
        return Asset()
