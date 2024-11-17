from flask import render_template, request
from app import app
from app.db.models import (
    Session,
    Lesson,
    Group
)




@app.get('/lessons/')
def lesson_get():
    with Session() as session:
        data = session.query(Lesson).all()
        groups = session.query(Group).all()
    return render_template('lesson/management.html', iterable=data, groups=groups)


@app.post('/lessons/')
def lesson_management():
    with Session() as session:
        session.add(Lesson(title=request.form.get('theme')))
        session.commit()
        data = session.query(Lesson).all()
        groups = session.query(Group).all()
    return render_template('lesson/management.html', iterable=data, groups=groups)


