import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://postgres:postgres@localhost:5432/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(debug=True)
