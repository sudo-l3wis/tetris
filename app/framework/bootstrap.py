from . import Kernel
from . container import Container, ModuleLoader
from . factory import AbstractFactory
from . singleton import App
from . service.parser import KeyParser
from . singleton import Config


factory = AbstractFactory()

container = Container()
container.set_modules(ModuleLoader().load())
container.set_factory(factory)

kernel = container.resolve(Kernel)
kernel.register()

parser = container.resolve(KeyParser)

application = container.resolve(App)
application.set_kernel(kernel)
application.set_container(container)
application.set_parser(parser)
