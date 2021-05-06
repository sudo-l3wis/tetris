class inject:
    """Class Injector Decorator.
    Instantiates & injects a class and it's dependencies resolved from the given
    key. The module, class & dependencies are mapped in config/modules.yaml and
    are instantiated via reflection or provided by an object pool if an item of
    the corresponding type exists.
    """

    def __init__(self, keys=False):
        """Set module key.
        :param keys: The module key
        """
        self.keys = keys

    def __call__(self, f):
        """Instantiate & inject the given class into the contextual function.
        :param f: The method to invoke.
        """

        def w(*args, **kwargs):
            if not isinstance(self.keys, list):
                self.keys = [self.keys]

            for key in self.keys:
                clazz = resolve(key)
                args = args + (clazz,)

            return f(*args, **kwargs)

        return w
