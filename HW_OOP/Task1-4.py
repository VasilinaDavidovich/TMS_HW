# Строки в Питоне сравниваются на основании значений символов. Т.е. если мы
# захотим выяснить, что больше: Apple или Яблоко, – то Яблоко окажется
# бОльшим. А все потому, что английская буква A имеет значение 65 (берется из
# таблицы кодировки), а русская буква Я – 1071. Надо создать новый класс
# RealString, который будет принимать строку и сравнивать по количеству
# входящих в них символов. Сравнивать между собой можно как объекты класса,
# так и обычные строки с экземплярами класса RealString.

from functools import total_ordering

@total_ordering
class RealString:
    def __init__(self, words: str):
        self.words = words

    # def length(self):
    #     return len(self.words)

    def __eq__(self, other):
        if isinstance(other, RealString):
            return len(self.words) == len(other.words)
        elif isinstance(other, str):
            return len(self.words) == len(other)

    def __lt__(self, other):
        if isinstance(other, RealString):
            return len(self.words) < len(other.words)
        elif isinstance(other, str):
            return len(self.words) < len(other)

str1 = RealString(words="Apple")
str2 = RealString(words="Cat")
str3 = "Pancake"

print(str1 > str3)