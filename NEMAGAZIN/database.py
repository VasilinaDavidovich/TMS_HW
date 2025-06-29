from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base, Product, Ticket, User
import uuid

DATABASE_URL = "sqlite:///shop.db"


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    def create_database(self):
        try:
            Base.metadata.create_all(self.engine)
            self._create_test_data()
            print("База создана успешно!")
            return True
        except Exception as e:
            print(f"Ошибка создания базы: {e}")
            return False

    def _create_test_data(self):
        session = self.Session()

        if not session.get(User, 1):
            session.add(User(id=1, username='admin', password='password'))
            session.commit()

        if not session.query(Product).first():
            session.add_all([
                Product(name="Телефон", cost=100, count=10),
                Product(name="Ноутбук", cost=300, count=5),
                Product(name="Наушники", cost=50, count=20)
            ])

        if not session.query(Ticket).first():
            session.add_all([
                Ticket(uuid=str(uuid.uuid4()), available=True, user=1),
                Ticket(uuid=str(uuid.uuid4()), available=True, user=1),
                Ticket(uuid=str(uuid.uuid4()), available=True, user=1),
                Ticket(uuid=str(uuid.uuid4()), available=False, user=1)
            ])

        session.commit()

        print("Созданные тикеты:")
        tickets = session.query(Ticket).all()
        for ticket in tickets:
            print(f"UUID: {ticket.uuid}, Available: {ticket.available}, User: {ticket.user}")

        session.close()

db = Database()
