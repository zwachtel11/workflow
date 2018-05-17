from flask import Blueprint, request, render_template
from my_app.api_po.models import User, Log
from my_app import db



# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_main = Blueprint('main', __name__, url_prefix='/main')

# Set the route and accepted methods
@mod_main.route('/timeline/', methods=['GET', 'POST'])

def main():
    test = []
    log = {}
    log['time'] = '1 pm'
    log['pagename'] = 'SearchResults.js'
    log['linenumber'] = '27'
    test.append(log)
    log1 = {}
    log1['time'] = '1 pm'
    log1['pagename'] = 'SearchResults.js'
    log1['linenumber'] = '27'
    test.append(log1)
    return render_template('main/timeline.html', search_result=test)
