# Создайте класс Soda (для определения типа газированной воды), принимающий
# 1 аргумент при инициализации (отвечающий за добавку к выбираемому
# лимонаду). В этом классе реализуйте метод show_my_drink(), выводящий на
# печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе
# отобразится следующая фраза: «Обычная газировка».

class Soda:
    def __init__(self, topping=None):
        self.topping = topping

    def show_my_drink(self):
        if self.topping:
            print(f"Газировка и {self.topping}")
        else:
            print("Обычная газировка")


drink1 = Soda(topping="Orange")
drink1.show_my_drink()

drink2 = Soda()
drink2.show_my_drink()
