from flask import Blueprint,redirect,url_for,render_template,flash
from modals.employee import Data
from extensions import db

from flask import request


deleteemp_bp = Blueprint('deletecontroller', __name__)


@deleteemp_bp.route("/delete/<int:id>", methods = ['GET','POST'])
def delete_employee(id):
    my_data= Data.query.get(id)
    db.session.delete(my_data)  
    db.session.commit()
    flash("Employee deleted successfully!")

    return redirect(url_for('index'))
        

