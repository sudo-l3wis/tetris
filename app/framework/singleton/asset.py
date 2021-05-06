from . singleton import MetaSingleton


class Asset(metaclass=MetaSingleton):
    def set_assets(self, assets):
        self.assets = assets

    def get_asset(self, asset):
        return self.assets[asset]
