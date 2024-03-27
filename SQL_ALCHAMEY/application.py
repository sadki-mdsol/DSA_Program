from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config.from_pyfile('config.cfg')

db = SQLAlchemy(app)

app.app_context().push()

class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)



if __name__ == '__main__':
    app.run()
