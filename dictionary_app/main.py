from dictionary_app.app import app
from dictionary_app.db_operations.person import get_person, create_person_table, put_person


@app.route("/<name>")
def get(name):
    return get_person(name)


@app.route("/create")
def create():
    create_person_table()
    return str(1)


@app.route("/put/<name>")
def put(name):
    p_id = put_person(name)
    return str(p_id)
