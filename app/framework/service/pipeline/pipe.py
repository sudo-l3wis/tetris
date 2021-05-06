class Pipe:

    def handle(self, resource, _next):
        """Process the pipe logic.
        :param resource: The instance to provide to each pipe.
        :param _next: A generator from which to resolve the next method.
        :return: The result of the next pipe invocation result.
        """
        return next(_next)(resource, _next)
