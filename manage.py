from __init__ import app, db
from flask_script import Manager, prompt_bool
from models import User, Book

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username='Matt', email='matthewmartinez1003@gmail.com'))
    db.session.add(Book(title='Wheel of Time', user_id=1))
    db.session.commit()
    print('Initialized the Database')


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to drop your database?"):
        db.drop_all()
        print('Dropped the Database')


if __name__ == '__main__':
    manager.run()
