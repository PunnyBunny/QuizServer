from flask import request
from server import app


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        id_ = request.form['id']
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        gender = request.form['gender']
        print(id_, name, date_of_birth, gender)
    return '<h1>hi<h1>'
