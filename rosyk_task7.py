import math as m


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"


class Vector:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.x = end.x - start.x
        self.y = end.y - start.y

    def __str__(self):
        return f'({self.start}, {self.end})'

    def length(self):
        return m.sqrt(self.x ** 2 + self.y ** 2)

    def add(self, vector):
        return Vector(self.start, Point(self.end.x + vector.x, self.end.y + vector.y))

    def subtract(self, vector):
        return Vector(self.start, Point(self.end.x - vector.x, self.end.y - vector.y))


if __name__ == '__main__':
    first_vector = Vector(Point(0, 0), Point(5, 8))
    second_vector = Vector(Point(9, 1), Point(6, 3))

    print(first_vector)
    print(first_vector.length())

    added_vector = first_vector.add(second_vector)
    subtracted_vector = first_vector.subtract(second_vector)
    print(added_vector, subtracted_vector)
