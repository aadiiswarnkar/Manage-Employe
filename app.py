from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from controllers import all_blueprints
from extensions import db
from modals.employee import Data
app = Flask(__name__)
app.secret_key =   'secret_key'

app.config.from_object(Config)

db.init_app(app) 





@app.route('/')
def index():
    all_employees = Data.query.all()
    return render_template('index.html',employees = all_employees)


for bp in all_blueprints:
    app.register_blueprint(bp)




if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Database tables created!")
    app.run(debug=True)