import math


class Figure:
    sides_count = 0

    def __init__(self, color: tuple[int, int, int], *sides, filled=False):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_color(r, g, b):
        valid_values = 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255
        valid_types = isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
        return valid_types and valid_values

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = (r, g, b)

    @staticmethod
    def __is__valid_sides(*sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *sides):
        if len(sides) == len(self.__sides):
            valid_sides = []
            for side in sides:
                if self.__is__valid_sides(side):
                    valid_sides.append(side)
            self.__sides = valid_sides


class Circle(Figure):
    def __init__(self, color: tuple[int, int, int], length, filled=False):
        super().__init__(color, length, filled=filled)
        self.__radius = length / (2 * math.pi)

    def get_square(self):
        S = math.pi * self.__radius ** 2
        return S


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color: tuple[int, int, int], *sides, filled=False, height):
        super().__init__(color, height, filled=filled)
        self.height = height

    def get_square(self):
        p = (len(self) / 2)
        sides = self.get_sides()
        return math.sqrt(p * (sides[0]) * (p - sides[1]) * (p - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple[int, int, int], *side, filled=False):
        cube_sides = [side for side in range(12)]
        super().__init__(color, *cube_sides, filled=filled)

    def get_volume(self):
        return self.get_sides()[6] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130))

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
