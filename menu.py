from sqlalchemy import select
from uuid import UUID
from models import User, Ticket, Product, Order
from typing import Optional
from sqlalchemy.orm import Session
from datetime import datetime

class Menu:
    def __init__(self, session: Session):
        self.session = session
        self.current_user: Optional[User] = None

    def show_main_menu(self):
        while True:
            print("\n=== Добро пожаловать в 'Не магазин!' ===")
            print("Команды: Товары, Зарегистрироваться, Войти")
            command = input("> ").strip().lower()
            if command == "товары":
                self.show_products()
            elif command == "зарегистрироваться":
                self.register_user()
            elif command == "войти":
                self.log_in_user()
            else:
                print("Неизвестная команда! Доступные команды: Товары, Зарегистрироваться, Войти")

    def show_products(self):
        products = self.session.query(Product).filter(Product.count > 0).order_by(Product.id).all()
        if not products:
            print("\nНет доступных товаров!")
            return
        print("\n"
              f"{'ID':<4} {'Стоимость':<10} {'Кол-во':<8} {'Название':<}")
        print("=" * 64)
        for product in products:
            print(f"{product.id:<4} {product.cost:<10} {product.count:<8} {product.name:<}")

    def register_user(self):
        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()
        if User.is_exist(self.session, username):
            print("Пользователь с таким именем уже существует!")
            return
        new_user = User(
            username=username,
            password=password,
            points=0
        )
        self.session.add(new_user)
        self.session.commit()
        self.current_user = new_user
        print(f"Добро пожаловать, {username}!")
        self.show_user_menu()

    def log_in_user(self):
        username = input("Введите логин: ").strip()
        password = input("Введите пароль: ").strip()
        if not User.is_exist(self.session, username):
            print("Пользователь с таким именем не существует!")
            return
        user = self.session.scalar(select(User).where(User.username == username))
        if user.password != password:
            print("Неверный пароль!")
            return
        self.current_user = user
        print(f"Добро пожаловать, {username}!")
        self.show_user_menu()

    def show_user_menu(self):
        while self.current_user:
            print('\n=== Добро пожаловать в "Не магазин!" ===')
            print('Здесь вы можете обменивать свои тикеты для того, чтобы приобретать товары\n')
            print('Для взаимодействия используйте команды:')
            print('> Товары')
            print('> Купить')
            print('> Профиль')
            print('> Тикет')
            command = input("> ").strip().lower()
            if command == "товары":
                self.show_products()
            elif command == "купить":
                self.process_purchase()
            elif command == "профиль":
                self.show_profile()
            elif command == "тикет":
                self.process_ticket()
            else:
                print("Доступные команды: Товары, Купить, Профиль, Тикет")

    def process_ticket(self):
        user_ticket = input("Введите UUID вашего тикета: ").strip()
        try:
            UUID(user_ticket)
        except ValueError:
            print("Неверный формат UUID!")
            return
        ticket = self.session.scalar(
            select(Ticket)
            .where(Ticket.uuid == user_ticket)
        )
        if not ticket:
            print("Билет не найден!")
            return
        if not ticket.available:
            print("Билет уже использован!")
            return
        self.current_user.points += 20
        ticket.available = False
        ticket.user_id = self.current_user.id
        self.session.commit()

    def process_purchase(self):
        user_purchase = int(input("Введите id товара, который хотите купить: "))
        quantity = int(input("Введите количество: "))
        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля!")
        product_to_buy = self.session.scalar(select(Product).where(Product.id == user_purchase))
        if not product_to_buy:
            print("Ошибка: товар не найден!")
            return
        if product_to_buy.count < quantity:
            print("На складе недостаточно товара")
            return
        prod_price = product_to_buy.cost
        summary = prod_price * quantity
        if self.current_user.points < summary:
            print("Недостаточно средств")
            return
        self.current_user.points -= summary
        product_to_buy.count -= quantity
        new_order = Order(
            user_id=self.current_user.id,
            product_id=product_to_buy.id,
            count=quantity,
            order_datetime=datetime.now())
        self.session.add(new_order)
        self.session.commit()

    def show_profile(self):
        print(f'\n=== {self.current_user.username} ===')
        print(f'\nПойнтов:{self.current_user.points}')
        print(f'\nЗаказы:')
        user_orders = self.current_user.orders(self.session)
        if not user_orders:
            print("У Вас пока нет заказов")
            return
        print(f"\n    {'Дата заказа':<20} {'Кол-во':<8} {'Сумма':<10} {'Товар':<}")
        print("    " + "-" * 50)
        for order in user_orders:
            product = self.session.get(Product, order.product_id)
            print(f"    {order.order_datetime.strftime('%H:%M %d.%m.%Y'):<20} "
                  f"{order.count:<8} "
                  f"{product.cost * order.count:<10} "
                  f"{product.name:<}")
