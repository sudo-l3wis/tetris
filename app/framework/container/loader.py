import os
import yaml


class ModuleLoader:

    def __init__(self):
        self.modules_path = './config/modules/'

    def load(self):
        """Load modules.
        :return: A list of modules.
        """
        modules = {}

        for root, dirs, files in os.walk(self.modules_path):
            for file in files:
                with open('{}/{}'.format(root, file)) as f:
                    modules.update(yaml.safe_load(f))

        return modules
