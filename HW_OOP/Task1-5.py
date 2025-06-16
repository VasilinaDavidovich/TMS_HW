# Напишите класс Rectangle, который имеет атрибуты: width (ширина) и
# height (высота). Класс должен иметь следующие методы:
# • Конструктор, который принимает два параметра: width и height, и
# инициализирует соответствующие атрибуты.
# • Метод str, который возвращает строковое представление объекта класса
# Rectangle в формате “Прямоугольник с шириной width и высотой
# height”.
# • Метод get_area, который возвращает площадь прямоугольника.
# • Метод get_perimeter, который возвращает периметр прямоугольника.
# • Метод is_square, который возвращает True, если прямоугольник является
# квадратом, и False в противном случае. Этот метод должен быть
# декорирован как property.


class Rectangle:

    def __init__(self, width: int | float, height: int | float):
        if not isinstance(width, int | float) or not isinstance(height, int | float):
            raise ValueError("Стороны прямоугольника должны выражаться в числах!")
        elif width <= 0 or height <= 0:
            raise ValueError("Стороны прямоугольника должны быть положительными числами!")
        self.width = width
        self.height = height

    def __str__(self):
        return f"Прямоугольник с шириной {self.width} и высотой {self.height}"

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.height + self.width) * 2


    @property
    def is_square(self):
        return self.width == self.height

rectangle1 = Rectangle(width=7, height=7)
print(rectangle1.is_square)