class ClassSpecification:

    def __init__(self, clazz):
        self.__clazz = clazz

    def get_key(self):
        """Get config key.
        :return: A config key resolved from the given class.
        """
        packages = self.__clazz.__module__.split('.')

        if len(packages) == 1:
            return self.__clazz.__name__.lower()

        elif len(packages) == 2:
            return packages[-1]

        return '{}.{}'.format(packages[-2], packages[-1])
