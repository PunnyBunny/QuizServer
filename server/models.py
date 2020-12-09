from server import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False, default=datetime.date.today())
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"User {self.name} id {self.id}"
