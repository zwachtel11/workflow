'''
This is the server init file ... when a user hits the endpoint this will respond.
'''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test6.db'
db = SQLAlchemy(app)
api = Api(app)
'''
from my_app.user.views import catalog
app.register_blueprint(catalog)
'''
from my_app.auth.controllers import mod_auth
app.register_blueprint(mod_auth)
 
db.create_all()