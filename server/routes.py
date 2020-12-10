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
            user = models.User(name=name, date_of_birth=date_of_birth, gender=gender)
            if not user.query.filter_by(name=name).first():
                db.session.add(user)
                db.session.commit()
            return actions.SUCCESS
        else:
            return actions.FAIL
    return '<h1>YO MAMA<h1>'
