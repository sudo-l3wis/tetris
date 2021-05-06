from . import ClassSpecification


class Container:
    __resolved = {}

    def set_modules(self, modules):
        """Set class modules.
        :param modules: The class definition modules.
        """
        self.modules = modules

    def set_factory(self, factory):
        """Set factory instance.
        :param factory: An abstract factory instance.
        """
        self.factory = factory

    def resolve(self, clazz):
        """Resolve the given class to an instance.
        :param clazz: The class to resolve.
        :return: An instance where by the type is relative to the class.
        """
        if clazz not in self.__resolved:
            spec = ClassSpecification(clazz)
            self.__resolved[clazz] = spec
        else:
            spec = self.__resolved[clazz]

        conf = self.modules[spec.get_key()]

        return self.resolve_by_conf(conf)

    def resolve_by_key(self, key):
        """Resolve class by key.
        Instantiate &return an instance from the given config key.
        :param key: The config key.
        :return: An instance derived from the given key.
        """
        if key in self.modules:
            return self.resolve_by_conf(self.modules[key])

        return False

    def resolve_by_conf(self, conf):
        """Resolve class by config.
        :param conf: The class config.
        :return: An instance derived from the given config.
        """
        return self.factory.get(conf, self.modules)
