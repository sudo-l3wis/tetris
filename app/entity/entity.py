from abc import ABCMeta, abstractmethod


class Entity(metaclass=ABCMeta):
    def __init__(self):
        self.__name = ''
        self.__x = 0
        self.__y = 0
        self.__width = 0
        self.__height = 0

    @abstractmethod
    def update(self, delta):
        pass

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_x(self):
        return self.__x

    def inc_x(self, i):
        self.__x += i

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def inc_y(self, i):
        self.__y += i

    def set_y(self, y):
        self.__y = y

    def get_pos(self):
        return self.__x, self.__y

    def get_origin(self):
        x = self.get_x() + self.get_width() / 2
        y = self.get_y() + self.get_height() / 2
        return x, y

    def set_pos(self, x, y):
        self.__x = x
        self.__y = y

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def intersects(self, pos):
        x, y = pos
        if self.get_x() >= x and self.get_x() <= x:
            if self.get_y() >= y and self.get_y() <= y:
                return True
        return False
