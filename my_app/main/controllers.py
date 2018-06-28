from __future__ import print_function
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from my_app.api_po.models import User, Log
from my_app import db
from my_app.main.forms import NotesForm
import sys
from my_app.api_po.views import UserApi


def get_logs(id):
    td = UserApi()
    td.post()
    return td.get(id)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_main = Blueprint('main', __name__, url_prefix='/main')

# Set the route and accepted methods
@mod_main.route('/timeline/', methods=['GET', 'POST'])

def main():
    form = NotesForm(request.form)
    logs = get_logs(1)[::-1]
    if form.validate_on_submit():
        test = Log.query.filter_by(id=int(request.form.get("my_id","").replace("#", ""))).first()
        test.note = form.message.data
        db.session.add(test)
        db.session.commit()
        return redirect(url_for('main.main'))


    return render_template('main/timeline.html', search_result=logs, form=form)
