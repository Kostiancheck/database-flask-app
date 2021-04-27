from dictionary_app.models.person import Person
from dictionary_app.app import db


def create_person_table():
    db.session.execute("CREATE TABLE Person (id SERIAL, name VARCHAR(512))")
    return "jopa"


def get_person(name):
    res = db.session.query(Person).filter(Person.name == name).first()
    if res:
        return str(res.id) + " " + str(res.name)
    else:
        return f"Name {name} doesn't exist"


def put_person(name):
    p = Person(name)
    db.session.add(p)
    db.session.commit()
    return "Id is " + str(p.id)
