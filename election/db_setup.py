from election.db import db, User, Position, Division, Suggestion, Question, Vote, Candidate, init_db
from flask import Flask
import os

def delete():
    if(os.path.exists("db.sqlite3")):
        os.remove("db.sqlite3")

def reinit():
    delete()
    db.create_all()

reinit()

tempD = Division(division_name = 'IT')
db.session.add(tempD)
tempD2 = Division(division_name = 'CM')
db.session.add(tempD2)
db.session.commit()
tempP = Position(position_name='manager')
db.session.add(tempP)
tempP = Position(position_name='staff')
db.session.add(tempP)
db.session.commit()
tempC = Candidate(candidate_name= 'cis', candidate_vision='ingin resign', candidate_mission='manejadikan semua wibu', candidate_blueprint='sldkasd.com', candidate_video='lasdasd.com')
db.session.add(tempC)
tempC2 = Candidate(candidate_name= 'no', candidate_vision='ingin resign', candidate_mission='manejadikan semua wibu', candidate_blueprint='sldkasd.com', candidate_video='lasdasd.com')
db.session.add(tempC2)
tempC3 = Candidate(candidate_name= 'kev', candidate_vision='ingin resign', candidate_mission='manejadikan semua wibu', candidate_blueprint='sldkasd.com', candidate_video='lasdasd.com')
db.session.add(tempC3)
db.session.commit()
q1 = Division.query.filter_by(division_name = 'IT').first()
q2 = Division.query.filter_by(division_name = 'CM').first()
q3 = Position.query.filter_by(position_name = 'manager').first()
q4 = Position.query.filter_by(position_name = 'staff').first()
tempU = User(name= 'alek', NIM='230120938', POB='jkt', DOB='14 Desember 2000', email='alex@gmail.com', vote=1, password='jkt141200', position_id=q3.position_id, division_id=q2.division_id)
db.session.add(tempU)
tempU2 = User(name= 'aric', NIM='2301890314', POB='jkt', DOB='14 Desember 2000', email='alex@gmail.com', vote=1, password='jkt141200', position_id=q4.position_id, division_id=q2.division_id)
db.session.add(tempU2)
tempU3 = User(name= 'adit', NIM='230120938', POB='jkt', DOB='14 Desember 2000', email='alex@gmail.com', vote=1, password='jkt141200', position_id=q4.position_id, division_id=q1.division_id)
db.session.add(tempU3)
tempU4 = User(name= 'tip', NIM='230120938', POB='jkt', DOB='14 Desember 2000', email='alex@gmail.com', vote=1, password='jkt141200', position_id=q4.position_id, division_id=q1.division_id)
db.session.add(tempU4)
db.session.commit()
tempq = Question(user_id = 1 , candidate_id = 1, question_subject = 'nama', question_body = 'siapa nama saya')
db.session.add(tempq)
db.session.commit()
tempV = Vote(user_id = 1, candidate_id = 1)
db.session.add(tempV)
tempV = Vote(user_id = 2, candidate_id = 1)
db.session.add(tempV)
tempV = Vote(user_id = 3, candidate_id = 2)
db.session.add(tempV)
db.session.commit()
tempC3 = Candidate(candidate_name= 'tip', candidate_vision='ingin resign', candidate_mission='manejadikan semua wibu', candidate_blueprint='sldkasd.com', candidate_video='lasdasd.com')
db.session.add(tempC3)
db.session.commit()

