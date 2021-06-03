from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os


### Uncomment this for the setup or if you want to test ###
app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)

# Comment this if you want to setup or test
# db = SQLAlchemy()
def init_db(app):
    app = app
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    db.init_app(app)
    
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(100), nullable=False)
    NIM     = db.Column(db.String(15), nullable=False)
    POB     = db.Column(db.String(50), nullable=False)
    DOB     = db.Column(db.String(50), nullable=False)
    email   = db.Column(db.String(50), nullable=False)
    vote    = db.Column(db.Integer, nullable=False)
    password= db.Column(db.String(50), nullable=False)

    # Foreign Key
    position_id = db.Column(db.Integer, db.ForeignKey('position.position_id'), nullable=False)
    division_id = db.Column(db.Integer, db.ForeignKey('division.division_id'), nullable=False)

    # Relationship
    suggestions  = db.relationship('Suggestion', backref='user', lazy=True)
    questions    = db.relationship('Question', backref='user', lazy = True)
    votes        = db.relationship('Vote', backref='user', lazy = True, uselist = False)

class Position(db.Model):
    position_id     = db.Column(db.Integer, primary_key=True)
    position_name   = db.Column(db.String(120), nullable=False)

    # relationship
    positions       = db.relationship('User', backref='position', lazy=True)

class Division(db.Model):
    division_id     = db.Column(db.Integer, primary_key=True)
    division_name   = db.Column(db.String(120), nullable=False)

    # relationship
    divisions       = db.relationship('User', backref='division', lazy=True)

class Suggestion(db.Model):
    suggestion_id         = db.Column(db.Integer, primary_key=True)
    suggestion_name       = db.Column(db.String(50), nullable=False)
    suggestion_division   = db.Column(db.String(50), nullable=False)

    #Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

class Candidate(db.Model):
    candidate_id     = db.Column(db.Integer, primary_key=True)
    candidate_name   = db.Column(db.String(50), nullable=False)
    candidate_vision   = db.Column(db.Text, nullable=False)
    candidate_mission  = db.Column(db.Text, nullable=False)
    candidate_blueprint= db.Column(db.String(200), nullable=False)
    candidate_video    = db.Column(db.String(100), nullable=False)

    #relationship
    questions    = db.relationship('Question', backref='candidate', lazy = True)
    votes        = db.relationship('Vote', backref='candidate', lazy = True)

class Question(db.Model):
    question_id             = db.Column(db.Integer, primary_key=True)
    question_time_stamp     = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    question_subject        = db.Column(db.String, nullable=False)
    question_body           = db.Column(db.Text, nullable=False)

    #Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.candidate_id'), nullable=False)

class Vote(db.Model):
    vote_id             = db.Column(db.Integer, primary_key=True)
    
    #Foreign Key
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False, unique=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.candidate_id'), nullable=False)
