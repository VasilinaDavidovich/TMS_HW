# Необходимо создать класс KgToPounds, в который принимает количество
# килограмм, а с помощью метода to_pounds() они переводятся в фунты.
# Необходимо закрыть доступ к переменной kg.
# Также, реализовать методы: - set_kg() - для задания нового значения килограммов (записывать только
# числовые значения),  - get_kg() - для вывода текущего значения кг.


class KgToPounds:
    def __init__(self, kg: int | float):
        self._kg = kg

    def get_kg(self):
        return self._kg

    def set_kg(self, new_kg):
        if not isinstance(new_kg, int | float):
            raise ValueError("Нужно вводить только числа!")
        else:
            self._kg = new_kg

    def to_pounds(self):
        pound = self._kg * 2.20462
        return pound


kilos = KgToPounds(kg=5)
print(kilos.set_kg(8))

# Второй вариант с декораторами будет в файле Task1-3.2