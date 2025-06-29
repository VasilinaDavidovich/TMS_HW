from database import db
from menu import Menu

def run_app():
    db.create_database()
    session = db.Session()
    menu = Menu(session)
    menu.show_main_menu()
    session.close()

run_app()
