import importlib

from app.framework.exception import ClassInstantiationError


class AbstractFactory:

    def get(self, conf, modules):
        """Get class instance with the given module config.
        :param conf: Module config.
        :param modules: The application modules.
        :return: An instance resolved from the given config.
        """
        clazz = conf['class']
        module = conf['module']
        dependencies = self.__get_dependencies(conf, modules)

        instance = self.__get__instance(clazz, module, dependencies)

        self.__invoke_methods(instance, conf, modules)

        return instance

    def __get_dependencies(self, conf, modules):
        """Resolve class dependencies from class specification.
        :param conf: The class specification from which to resolve.
        :param modules: The application modules.
        :return: A tuple of class dependency instances.
        """
        dependencies = ()

        if 'dependencies' in conf:
            for dependency in conf['dependencies']:
                dependency_conf = modules[dependency]
                dependencies += (self.get(dependency_conf, modules),)

        return dependencies

    def __get__instance(self, clazz, module, dependencies):
        """Get class instance.
        :param clazz: The class to instantiate.
        :param module: The module that the class belongs to.
        :param dependencies: The dependencies to inject into the class.
        :return: The instantiated instance.
        """
        try:
            _module = importlib.import_module(module)
            return getattr(_module, clazz)(*dependencies)

        except Exception as e:
            raise ClassInstantiationError(clazz, str(e))

    def __invoke_methods(self, instance, conf, modules):
        """Invoke instance methods.
        :param instance: The instance on which to invoke methods.
        :param conf: The instance class specification.
        :param modules: The application class specifications.
        """
        if 'methods' in conf:
            for method in conf['methods']:
                self.__resolve_and_invoke_method(instance, method, modules)

    def __resolve_and_invoke_method(self, instance, method, modules):
        """Resolve & invoke the given method.
        Resolve the given method & it's dependencies then invoke it.
        :param instance: The instance on which to invoke methods.
        :param conf: The instance class specification.
        :param modules: The application class specifications.
        """
        if isinstance(method, str):
            getattr(instance, method)()

        elif isinstance(method, dict):
            _dependencies = ()

            for key, dependencies in method.items():
                for dependency in dependencies:
                    _dependency = self.get(modules[dependency], modules)
                    _dependencies += (_dependency,)

                getattr(instance, key)(*_dependencies)
