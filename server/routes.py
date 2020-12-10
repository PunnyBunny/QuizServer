from datetime import datetime

from flask import request

from server import app, actions, models, db


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        action = request.form['action']
        if action == actions.ADD_NEW:
            name = request.form['name']
            date_of_birth = datetime.strptime(request.form['date_of_birth'], '%d-%m-%Y').date()
            gender = request.form['gender']
            score = int(request.form['score'])
            test_name = request.form['test_name']
            test_full_score = request.form['test_full_score']

            person = models.Person.query.filter_by(name=name, date_of_birth=date_of_birth, gender=gender).first()
            if not person:
                person = models.Person(name=name, date_of_birth=date_of_birth, gender=gender)
                db.session.add(person)

            test = models.Test.query.filter_by(name=test_name, full_score=test_full_score).first()
            if not test:
                test = models.Test(name=test_name, full_score=test_full_score)
                db.session.add(test)

            result = models.TestResult(score=score, person=person, test=test)

            db.session.add(result)
            db.session.commit()

            return actions.SUCCESS
        else:
            return actions.FAIL
    return '<h1>YO MAMA<h1>'
