# Во второй версии необходимо использовать декоратор property для создания
# setter и getter взамен set_kg и get_kg.

class KgToPounds:
    def __init__(self, kg: int | float):
        self._kg = kg

    @property
    def kg(self):
        return self._kg

    @kg.setter
    def kg(self, new_kg):
        if not isinstance(new_kg, int | float):
            raise ValueError("Нужно вводить только числа!")
        self._kg = new_kg

    def to_pounds(self):
        pound = self._kg * 2.20462
        return pound


kilos = KgToPounds(kg=5)
kilos.kg = 9
print(kilos.kg)