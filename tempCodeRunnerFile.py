from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
# from config import Config

app = Flask(__name__)
app.secret_key =   'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/manageemp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config.from_object(Config)

db = SQLAlchemy(app)



class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(100),nullable = False, unique = True)
    phone = db.Column(db.String(15),nullable = False, unique = True)

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)