from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)


    @staticmethod
    def init_db_users():
        user_one = User(first_name='Hello', last_name='World', email='helloworld@icloud.com', password='password123')

        user_two = User(first_name='Uncle', last_name='Bob', email='bobthebuilder@email.com', password='GoClEaNyOuRcOdE')

        user_three = User(first_name='Good', last_name='Neighbor', email='jake@statefarm.com', password='khaki$')

        user_four = User(first_name='Karen', last_name='Also-Karen', email='karen@karenassociation.com', password='managerN0W')

        user_five = User(first_name='Vulnerable', last_name='Account', email='administration@gmail.com', password='10987654321')

        db.session.add_all([user_one, user_two, user_three, user_four, user_five])
        db.session.commit()