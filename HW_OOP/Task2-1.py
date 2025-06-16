# Создать класс Matrix, который будет реализовывать следующие возможности.
# Класс должен принимать список списков.
# Например:
# m = Matrix([[-1, 3], [0, 1], [-2, 2]])
# будет представлять матрицу
# Пункты синего цвета означают методы, которые должны возвращать
# новый экземпляр класса Matrix.
# Пункты зеленого цвета — это методы основанные на @classmethod
# • Сложение матриц (только одинаковых размерностей):
# • Вычитание матриц (точно так же).
# • Умножение матрицы на число.
# • Транспонирование матрицы:
# Пример:
# • Создает единичную матрицу размером m, n
# • Создает нулевую матрицу размером m, n
# • Создает диагональную матрицу из переданного списка
# • Возвращает размерность матрицы (кортеж)
# • Возвращает кол-во элементов в матрице
# • Возвращает сумму всех элементов матрицы
# • Возвращает новую матрицу, где вместо отрицательных чисел стоят нули
# • Возможность сравнения на равенство двух матриц
# • Переопределить метод __str__

class Matrix:
    def __init__(self, data: list):
        self.data = data
        self.rows = len(data)
        self.columns = len(data[0])

    def __str__(self):
        return f"{self.data}"

    # Сложение матриц (только одинаковых размерностей)
    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Нельзя сложить матрицы разного размера!")
        res = []
        for el in range(self.rows):
            row = []
            for element in range(self.columns):
                row.append(self.data[el][element] + other.data[el][element])
            res.append(row)
        return Matrix(res)

    # • Вычитание матриц (точно так же)
    def __sub__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise ValueError("Нельзя вычитать матрицы разного размера!")
        result = []
        for el in range(self.rows):
            row = []
            for element in range(self.columns):
                row.append(self.data[el][element] - other.data[el][element])
            result.append(row)
        return Matrix(result)

    # • Умножение матрицы на число.
    def __mul__(self, other: int | float):
        if not isinstance(other, int | float):
            raise ValueError("Умножать можно только на число!")
        res = []
        for el in range(self.rows):
            row = []
            for element in range(self.columns):
                row.append(self.data[el][element] * other)
            res.append(row)
        return Matrix(res)

    # • Транспонирование матрицы
    def transpose(self):
        res = []
        for element in range(self.columns):
            row = []
            for el in range(self.rows):
                new_el = self.data[el][element]
                row.append(new_el)
            res.append(row)
        return Matrix(res)

    # • Создает единичную матрицу размером m, n
    @classmethod
    def create_matrix(cls, m, n):
        matrix = []
        for el in range(m):
            row = []
            for element in range(n):
                if el == element:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return cls(matrix)

    # • Создает нулевую матрицу размером m, n
    @classmethod
    def create_zero_matrix(cls, m, n):
        matrix = []
        for el in range(m):
            row = []
            for element in range(n):
                row.append(0)
            matrix.append(row)
        return cls(matrix)

    # • Создает диагональную матрицу из переданного списка
    @classmethod
    def create_diag_matrix(cls, numbers : list):
        matrix = []
        n = len(numbers)
        for el in range(0, n):
            row = []
            for element in range(n):
                if el == element:
                    row.append(numbers[el])
                else:
                    row.append(0)
            matrix.append(row)
        return cls(matrix)

    # • Возвращает размерность матрицы (кортеж)
    def size(self):
        return (self.rows, self.columns)

    # • Возвращает кол-во элементов в матрице
    def elements_quantity(self):
        return self.rows * self.columns

    # • Возвращает сумму всех элементов матрицы
    def sum_of_elements(self):
        sum_el = 0
        for el in range(self.rows):
            for element in range(self.columns):
                sum_el += self.data[el][element]
        return sum_el

    # • Возвращает новую матрицу, где вместо отрицательных чисел стоят нули
    def make_no_negative(self):
        new_matrix = []
        for el in range(self.rows):
            row = []
            for element in range(self.columns):
                if self.data[el][element] < 0:
                    row.append(0)
                else:
                    row.append(self.data[el][element])
            new_matrix.append(row)
        return Matrix(new_matrix)

    # • Возможность сравнения на равенство двух матриц
    def __eq__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Матрицу можно сравнивать только с матрицей!")
        if self.rows != other.rows or self.columns != other.columns:
            return False
        for el in range(self.rows):
            for element in range(self.columns):
                if self.data[el][element] != other.data[el][element]:
                    return False
        return True

    # • Переопределить метод __str__
class NewMatrix(Matrix):
    def __str__(self):
        return f"Новая матрица: {self.data}"

m = Matrix([[-1, 3], [0, 1], [-2, 2]])
m1 = Matrix([[-1, 3], [0, 1], [-2, 2]])
m3 = Matrix.create_diag_matrix([1, 2, 3, 4])
m4 = NewMatrix([[1, 1], [0, 5]])
print(m1.__eq__(m))
print(m4)
