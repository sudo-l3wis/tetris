from . singleton import MetaSingleton


class App(metaclass=MetaSingleton):

    def set_kernel(self, kernel):
        """Set kernel instance.
        :param kernel: A kernel instance.
        """
        self.kernel = kernel

    def set_container(self, container):
        """Set container instance.
        :param container: A service container.
        """
        self.container = container

    def set_parser(self, parser):
        """Set parser instance.
        :param parser: An object parser instance.
        """
        self.parser = parser

    def get(self, key):
        """Parse & return the given attribute.
        :param key: The key of the attribute to parse.
        :return: The attribute value.
        """
        return self.parser.parse(key, self)
