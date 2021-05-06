class ClassInstantiationError(RuntimeError):
    def __init__(self, clazz, message):
        """Error instantiating class.
        This error is thrown when an exception is raised while
        attempting to instantiate a class via the container factory.
        """
        super().__init__('Error instantiating class {}. {}.'.format(clazz, message))
