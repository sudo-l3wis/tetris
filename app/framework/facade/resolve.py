from . import AbstractFacade


class ResolveFacade(AbstractFacade):

    def __init__(self):
        super().__init__('resolve')

    def invoke(self, clazz):
        if isinstance(clazz, str):
            return app('container').resolve_by_key(clazz)
        return app('container').resolve(clazz)
