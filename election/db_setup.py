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
tempU70 = User(name= 'Tiffany Ciangsawira', NIM='2301860444', POB='Jakarta', DOB='23 Maret 2001', email='gracia.tiffany@gmail.com', vote=1, password='jakarta23032001', position_id=3, division_id=8)
tempU71 = User(name= 'Aditya', NIM='2301914270', POB='Gorontalo', DOB='3 Juni 2001', email='adityasaroinsong@gmail.com', vote=1, password='gorontalo03062001', position_id=2, division_id=8)
tempU72 = User(name= 'Alexander Dennis Suwardi', NIM='2301862853', POB='Jakarta', DOB='14 Desember 2000', email='swrddennis@gmail.com', vote=1, password='jakarta14122000', position_id=2, division_id=8)
tempU73 = User(name= 'Aric Hernando', NIM='2301890314', POB='Pekanbaru', DOB='13 November 2001', email='hernandoaric@gmail.com', vote=1, password='pekanbaru13112001', position_id=2, division_id=8)
tempU74 = User(name= 'Ivano Ekasetia', NIM='2301863345', POB='Mojokerto', DOB='3 Maret 2001', email='ivanoekasetia@gmail.com', vote=1, password='mojokerto03032001', position_id=1, division_id=8)
tempU75 = User(name= 'Alexandre Christian Ady Wijaya', NIM='2440041806', POB='Makassar', DOB='22 Maret 2003', email='alexandre.228.c.a.w@gmail.com', vote=1, password='makassar22032003', position_id=1, division_id=8)
tempU76 = User(name= 'Christian Michael Putra Mandala', NIM='2440020442', POB='Purbalingga', DOB='10 Juni 2002', email='christianmichaelputramandala@gmail.com', vote=1, password='purbalingga10062002', position_id=1, division_id=8)
tempU77 = User(name= 'Francis Alexander', NIM='2440062161', POB='Surabaya', DOB='22 Agustus 2002', email='francisalexander02@gmail.com', vote=1, password='surabaya22082002', position_id=1, division_id=8)
tempU78 = User(name= 'Kevin Wijaya', NIM='2440020921', POB='Samarinda', DOB='2 Oktober 2002', email='kevinwijaya572@gmail.com', vote=1, password='samarinda2102002', position_id=1, division_id=8)
db.session.add(tempU0)
db.session.add(tempU70)
db.session.add(tempU71)
db.session.add(tempU72)
db.session.add(tempU73)
db.session.add(tempU74)
db.session.add(tempU75)
db.session.add(tempU76)
db.session.add(tempU77) 
db.session.add(tempU78)
db.session.commit()