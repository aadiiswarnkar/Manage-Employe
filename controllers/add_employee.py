from flask import Blueprint,redirect,url_for,render_template,flash
from modals.employee import Data
from extensions import db

from flask import request


addemp_bp = Blueprint('addcontroller', __name__)


@addemp_bp.route("/add_employee", methods = ['POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        if name and email and phone:
            new_employee = Data(name, email, phone)
            db.session.add(new_employee)
            db.session.commit()
            flash("Employee added successfully!")
            return redirect(url_for('index'))
        else:
            return render_template('index.html', message = "Please fill all fields!")
        

