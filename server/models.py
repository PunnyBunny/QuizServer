from server import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    test_results = db.relationship('TestResult', backref='person')

    def __repr__(self):
        return f"Person (id={self.id}) (name={self.name}) (date_of_birth={self.date_of_birth}) (gender={self.gender})"

    def __str__(self):
        return self.__repr__()


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    full_score = db.Column(db.Integer, nullable=False)
    results = db.relationship('TestResult', backref='test')

    def __repr__(self):
        return f'Test {id}'


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)

    def __repr__(self):
        return f'{str(self.person)} score={self.score}'

