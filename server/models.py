from server import db


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    school_name = db.Column(db.String(50), nullable=False)
    grade_level = db.Column(db.String(2), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    test_results = db.relationship('TestResult', backref='person')

    def __repr__(self):
        return f"Person (id={self.id}) (name={self.name}) (date_of_birth={self.date_of_birth}) (gender={self.gender})"

    def __str__(self):
        return self.__repr__()


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    length = db.Column(db.Integer, nullable=False)
    type_ = db.Column(db.String(5), nullable=False)
    results = db.relationship('TestResult', backref='test')

    def __repr__(self):
        return f'Test {id}'


class TestResult(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Integer)
    filename = db.Column(db.String(50))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey('test.id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'{str(self.person)} score={self.score}'

