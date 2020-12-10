from server import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)

    def __repr__(self):
        return f"User (id={self.id}) (name={self.name}) (date_of_birth={self.date_of_birth}) (gender={self.gender})"
