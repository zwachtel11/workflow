'''
This is the server init file ... when a user hits the endpoint this will respond.
'''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api



app = Flask(__name__)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test9.db'
db = SQLAlchemy(app)
api = Api(app)

from my_app.api_po.views import api_point
app.register_blueprint(api_point)

from my_app.auth.controllers import mod_auth
app.register_blueprint(mod_auth)

from my_app.main.controllers import mod_main
app.register_blueprint(mod_main)
 
db.create_all()