from election.db import db, User, Position, Division, Suggestion, Question, Vote, Candidate
db.create_all()

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

### Uncomment this to simulate votes ###

# tempv = Vote(user_id = 1, candidate_id = 3)
# db.session.add(tempv)
# tempv2 = Vote(user_id = 2, candidate_id = 1)
# db.session.add(tempv2)
# tempv3 = Vote(user_id = 3, candidate_id = 2)
# db.session.add(tempv3)
# tempv4 = Vote(user_id = 4, candidate_id = 3)
# db.session.add(tempv4)
# db.session.commit()

# user = User.query.filter_by(name = 'alek').first()
# user.vote = 0
db.session.commit()


# User.query.join(Division, User.division_id == Division.division_id).filter_by(division_name = 'IT').all()

# db.session.query(Candidate, db.func.count(Vote.vote_id).label('count')).join(Vote, Candidate.candidate_id == Vote.candidate_id).group_by(Candidate.candidate_name).order_by(db.func.count(Vote.vote_id).desc()).first()