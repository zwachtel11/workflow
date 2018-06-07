from my_app import db
import datetime
 
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    logs = db.relationship('Log', backref='user', uselist=True, lazy=True)
 
    def __init__(self, name, password):
        self.name = name
        self.password = password
 
    def __repr__(self):
        return '<User %d>' % self.id

    def get_count(self):
        return len(self.logs)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pagename = db.Column(db.String(255))
    note = db.Column(db.String(255))
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, pagename, person_id, pagenumber):
        self.pagename = pagename
        self.pagenumber = pagenumber
        self.person_id = person_id
        self.note = ''
    def __repr__(self):
        return '<Log %d>' % self.id