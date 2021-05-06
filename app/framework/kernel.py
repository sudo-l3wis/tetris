class Kernel:
    def __init__(self, *providers):
        self.providers = providers

    def register(self):
        for provider in self.providers:
            provider.register()
