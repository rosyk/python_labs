import math as m


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector:
    def __init__(self, start, end):
        self.__start = start
        self.__end = end
        self.__x = end.x - start.x
        self.__y = end.y - start.y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def length(self):
        return m.sqrt(self.__x ** 2 + self.__y ** 2)

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    def __add__(self, vector):
        return Vector(self.__start, Point(self.__end.x + vector.x, self.__end.y + vector.y))

    def __sub__(self, vector):
        return Vector(self.__start, Point(self.__end.x - vector.x, self.__end.y - vector.y))


if __name__ == '__main__':
    first_vector = Vector(Point(0, 0), Point(5, 8))
    second_vector = Vector(Point(9, 1), Point(6, 3))

    print(first_vector)
    print(first_vector.length)

    print(first_vector + second_vector, first_vector - second_vector)
