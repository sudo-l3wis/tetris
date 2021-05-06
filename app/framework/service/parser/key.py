from . import AbstractParser


class KeyParser(AbstractParser):

    def parse(self, _key, instance):
        """Parse key.
        Parse the given period delimited string and return the
        associated instance within the given instance.
        :param _key: The key to parse.
        :param instance: The instance to search.
        :return: An property retrieved from the given instance.
        """
        keys = _key.split('.')

        for key in keys:
            if isinstance(instance, dict):
                if key in instance:
                    instance = instance[key]
                else:
                    return False

            elif isinstance(instance, object):
                if hasattr(instance, key):
                    instance = getattr(instance, key)
                else:
                    return False

        return instance
