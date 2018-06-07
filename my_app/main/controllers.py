from __future__ import print_function
from flask import Blueprint, request, render_template
from my_app.api_po.models import User, Log
from my_app import db
import sys
from my_app.api_po.views import UserApi


def get_logs(id):
    td = UserApi()
    td.post()
    test = []
    return td.get(13)

def tester_fill():
    log = {}
    test = []
    log['time'] = '1 pm'
    log['pagename'] = 'SearchResults.js'
    log['linenumber'] = '27'
    log['note'] = 'fasdljkfsdl;fjds dsajklfdsjlfsd;fdjslfkj dsaflksdfjdsf;sd'
    test.append(log)
    log1 = {}
    log1['time'] = '1 pm'
    log1['pagename'] = 'SearchResults.js'
    log1['linenumber'] = '27'
    log1['note'] = 'fasdljkfsdl;fjds dsajklfdsjlfsd;fdjslfkj dsaflksdfjdsf;sd'
    test.append(log1)

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_main = Blueprint('main', __name__, url_prefix='/main')

# Set the route and accepted methods
@mod_main.route('/timeline/', methods=['GET', 'POST'])

def main():
    logs = get_logs(13)
    logs[0].note = 'Sometimes I sit and think'
    print(logs[0].note, file=sys.stdout)

    return render_template('main/timeline.html', search_result=logs)
