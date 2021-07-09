from db import db, User, Position, Division, Suggestion, Question, Vote, Candidate, init_db
from flask import Flask
import os

def delete():
    if(os.path.exists("db.sqlite3")):
        os.remove("db.sqlite3")

def reinit():
    delete()
    db.create_all()

reinit()

tempD = Division(division_name = 'Public Relation')
db.session.add(tempD)
tempD = Division(division_name = 'Culture')
db.session.add(tempD)
tempD = Division(division_name = 'Human Resource and Development')
db.session.add(tempD)
tempD = Division(division_name = 'Social')
db.session.add(tempD)
tempD = Division(division_name = 'Sport')
db.session.add(tempD)
tempD = Division(division_name = 'Creative Media')
db.session.add(tempD)
tempD = Division(division_name = 'ART')
db.session.add(tempD)
tempD = Division(division_name = 'Information Technology')
db.session.add(tempD)
tempD = Division(division_name = 'BSSC')
db.session.add(tempD)
db.session.commit()

tempP = Position(position_name='Junior Staff')
db.session.add(tempP)
tempP = Position(position_name='Senior Staff')
db.session.add(tempP)
tempP = Position(position_name='Manager')
db.session.add(tempP)
tempP = Position(position_name='Chairman')
db.session.add(tempP)
tempP = Position(position_name='EXCOM')
db.session.add(tempP)
tempP = Position(position_name='Advisor')
db.session.add(tempP)
db.session.commit()


tempC = Candidate(candidate_name= 'Ivano Ekasetia', candidate_vision='memajukan bssc', candidate_mission='meningkatkan kemampuan setiap anggota bssc', candidate_blueprint='https://www.youtube.com/embed/MJbE3uWN9vE', candidate_video='https://www.youtube.com/embed/MJbE3uWN9vE')
db.session.add(tempC)
tempC2 = Candidate(candidate_name= 'Francis Alexander', candidate_vision='memajukan bssc', candidate_mission='meningkatkan kemampuan setiap anggota bssc', candidate_blueprint='https://www.youtube.com/embed/MJbE3uWN9vE', candidate_video='https://www.youtube.com/embed/MJbE3uWN9vE')
db.session.add(tempC2)
tempC3 = Candidate(candidate_name= 'Kevin Wijaya', candidate_vision='memajukan bssc', candidate_mission='meningkatkan kemampuan setiap anggota bssc', candidate_blueprint='https://www.youtube.com/embed/MJbE3uWN9vE', candidate_video='https://www.youtube.com/embed/MJbE3uWN9vE')
db.session.add(tempC3)

tempU0 = User(name= 'Election Team', NIM='00000000', POB='-', DOB='-', email='-', vote=1, password='electionteam2021', position_id=2, division_id=8)
tempU72 = User(name= 'Alexander Dennis Suwardi', NIM='1', POB='Jakarta', DOB='14 Desember 2000', email='swrddennis@gmail.com', vote=1, password='a', position_id=2, division_id=8)
tempU73 = User(name= 'Aric Hernando', NIM='2', POB='Pekanbaru', DOB='13 November 2001', email='hernandoaric@gmail.com', vote=1, password='a', position_id=2, division_id=8)
db.session.add(tempU0)
db.session.add(tempU72)
db.session.add(tempU73)
db.session.commit()