from flask import Blueprint,redirect,url_for,render_template,flash
from modals.employee import Data
from extensions import db

from flask import request


update_bp = Blueprint('updatecontroller', __name__)



@update_bp.route("/update",methods = ['GET','POST'])
def update_employee():
    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.name = request.form['name']
        my_data.email = request.form['email']
        my_data.phone = request.form['phone']
        db.session.commit()
        flash("Employee updated successfully!")
        return redirect(url_for('index'))