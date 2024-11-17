from flask import render_template, request
from app import app
from app.db.models import (
    Session,
    Group,
)
from sqlalchemy import (
    select
)


@app.route('/groups/', methods=["GET", "POST"])
def group_management():
    with Session() as session:
        if request.method == "POST":
            session.add(Group(name=request.form.get('name')))
            session.commit()
        data = session.query(Group).all()

    return render_template('group/management.html', iterable=data)

@app.get("/groups/")
def group_get1():
    with Session() as session:
        data = session.query(Group).all()
    return render_template('group/management.html', iterable=data)



@app.get('/groups/<int:id>')
def group_get(id):
    with Session() as session:
        data = session.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template('main.html', content=data)

