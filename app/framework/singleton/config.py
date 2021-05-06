from . import MetaSingleton


class Config(metaclass=MetaSingleton):

    def __init__(self):
        self.parser = None

    def set_parser(self, parser):
        """Set attribute parser.
        :param parser: The parser strategy to user.
        """
        self.parser = parser

    def put(self, attr, value):
        """Attach the given attribute as a config property.
        :param attr: The attribute to attach.
        :param value: The attribute value.
        """
        setattr(self, attr, value)

    def get(self, key):
        """Parse & return the given attribute.
        :param key: The key of the attribute to parse.
        :return: The attribute value.
        """
        return self.parser.parse(key, self)
