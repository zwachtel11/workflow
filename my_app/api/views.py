from __future__ import print_function # In python 2.7
import sys
import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from flask.ext.restful import Resource
from flask.ext.restful import reqparse
from my_app import db, app, api
from my_app.user.models import User, Log
from my_app.auth import requires_auth 
 
api_point = Blueprint('api_point', __name__)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str)
parser.add_argument('password', type=str)
parser.add_argument('pagename', type=str)
parser.add_argument('pagenumber', type=float)


@api_point.route('/')
#@api_point.route('/home')
#@requires_auth
def home():
    users = User.query.paginate(1, 100).items
    res = {}
    for user in users:
        if str(request.authorization.username) == str(user.name):
            res['id'] = user.id
    return json.dumps(res)

def create_list(fruits):
    json_list = []
    for fruit in fruits:
        json_list.append(str(fruit.name) + ',' + str(fruit.created_date))
    return json_list
 
class UserApi(Resource):
    #@requires_auth
    def get(self, id=None, page=1):
        if not id:
            users = User.query.paginate(page, 100).items
        else:
            users = [User.query.get(id)]
        res = {}
        for user in users:
            res[user.id] = {
                'name': user.name,
                'log_count': str(user.get_count()),
                'created_date': str(user.created_date),
                'logs': create_list(user.logs),
            }
        return json.dumps(res)
 
    def post(self):
        args = parser.parse_args()
        name = args['name']
        password = args['password']
        user = User(name, password)
        db.session.add(user)
        db.session.commit()
        res = {}
        res[user.id] = {
            'name': user.name,
            'password': user.password,
            'created_date': str(user.created_date),
        }
        return json.dumps(res)
 
    def put(self, id):
        # Update the record for the provided id
        # with the details provided.
        args = parser.parse_args()
        pagenumber = args['pagenumber']
        pagename = args['pagename']

        users = [User.query.get(id)]
        res = {}
        for user in users:
            log = Log(pagename, pagenumber, user.id)
            db.session.add(log)
            user.logs.append(log)
            db.session.commit()
            res[user.id] = {
                'name': user.name,
                'new_log': log,
                'log_count': str(user.get_count()),
            }
            
        return json.dumps(res)

    def delete(self, id):
        # Delete the record for the provided id.
        return
 
api.add_resource(
   UserApi,
   '/api/user',
   '/api/user/<int:id>',
   '/api/user/<int:id>/<int:page>'
)