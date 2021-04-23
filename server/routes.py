import os
from datetime import datetime

from flask import request

from server import app, actions, models, db


@app.route('/', methods=['POST', 'GET'])
def home():
    """
    type: 'audio' or 'mc'
    name: name of participant
    date_of_birth: date of birth of participant in DD-MM-YYYY format
    gender: gender of participant ('m' or 'f')
    school_name: name of school of participant
    grade_level: grade level of participant

    test_name: name of the test
    full_score: length of the test

    audios: if type is 'audio' then an audios.zip containing the audio of the participant

    score: if type is 'mc' then score of participant in the test
    """
    if request.method == 'GET':
        return '''
            <!doctype html>
            <title>JOON GAY</title>
            <h1>JOON GAY</h1>
        '''

    type_ = request.form['type']
    name = request.form['name'].strip()
    date_of_birth = datetime.strptime(request.form['date_of_birth'], '%d-%m-%Y').date()
    gender = request.form['gender']
    school_name = request.form['school_name'].strip()
    grade_level = request.form['grade_level']

    test_name = request.form['test_name']
    length = int(request.form['length'])

    person = models.Person.query.filter_by(name=name, date_of_birth=date_of_birth, gender=gender,
                                           school_name=school_name, grade_level=grade_level).first()
    if not person:
        person = models.Person(name=name, date_of_birth=date_of_birth, gender=gender, school_name=school_name,
                               grade_level=grade_level)
        db.session.add(person)
        person = models.Person.query.filter_by(name=name, date_of_birth=date_of_birth, gender=gender,
                                               school_name=school_name, grade_level=grade_level).first()
    test = models.Test.query.filter_by(name=test_name, length=length, type_=type_).first()
    if not test:
        test = models.Test(name=test_name, length=length, type_=type_)
        db.session.add(test)
        test = models.Test.query.filter_by(name=test_name, length=length, type_=type_).first()
    timestamp = datetime.now()
    if type_ == 'audio':
        file = request.files['audios']
        print(person.grade_level)
        filename = f'{person.school_name}, {person.grade_level}, {person.name}, ({person.gender}), {test.name}, {timestamp.strftime("%Y-%m-%d %H-%M-%S")}.zip'
        print(filename)
        if not os.path.exists('audios'):
            os.mkdir('audios')
        file.save(os.path.join('audios', filename))
        result = models.TestResult(person=person, test=test, filename=filename, timestamp=timestamp)
    else:
        score = request.form['score']
        result = models.TestResult(person=person, test=test, score=score, timestamp=timestamp)

    db.session.add(result)
    db.session.commit()

    return actions.SUCCESS
