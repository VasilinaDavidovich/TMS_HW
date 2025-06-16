# Требуется проверить, возможно ли из представленных отрезков условной длины
# сформировать треугольник. Для этого необходимо создать класс
# TriangleChecker, принимающий только положительные числа. С помощью
# метода is_triangle() возвращаются следующие значения (в зависимости от
# ситуации): – Ура, можно построить треугольник!; – С отрицательными числами ничего не выйдет!;– Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать
from random import triangular


class TriangleChecker:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_triangle(self):
        if not (isinstance(self.side1, int | float)
                and isinstance(self.side2, int | float)
                and isinstance(self.side3, int | float)):
            raise ValueError("Нужно вводить только числа!")
        elif self.side1 <= 0 or self.side2 <= 0 or self.side3 <= 0:
            raise ValueError("С отрицательными числами ничего не выйдет!")
        elif (self.side1 + self.side2 <= self.side3
              or self.side2 + self.side3 <= self.side1
              or self.side1 + self.side3 <= self.side2):
            raise ValueError("Жаль, но из этого треугольник не сделать")
        else:
            print("Ура, можно построить треугольник!")

triangle1 = TriangleChecker(side1=5, side2=9, side3=6)
triangle1.is_triangle()