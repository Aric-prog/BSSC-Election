from db import db, User, Position, Division, Suggestion, Question, Vote, Candidate
import os

def delete():
    if(os.path.exists("db.sqlite3")):
        os.remove("db.sqlite3")

def reinit():
    delete()
    db.create_all()

# -> bool is the return type
def has_voted(user_id : int) -> bool:
    q = User.query.filter_by(user_id = user_id).first().vote
    if (q == 0):
        return True
    else :
        return False

def has_suggested(user_id : int) -> bool:
    q = Suggestion.query.join(User, Suggestion.user_id == User.user_id).filter_by(user_id = 1).count()
    if q == 0 :
        return False
    else :
        return True

# Returns the remaining vote for a user
def vote_amount(user_id : int) -> int:
    return User.query.filter_by(user_id = user_id).first().vote
 
def get_all_candidate() -> list:
    return Candidate.query.all()

def get_candidate(candidate_id : int) -> Candidate:
    return Candidate.query.filter_by(candidate_id = candidate_id).first()

# Returns the total amount of votes
def total_votes() -> int:
    return vote.query.count()

def most_voted_candidate() -> Candidate:
    q1 = db.session.query(Candidate, db.func.count(Vote.vote_id).label('count')).join(Vote, Candidate.candidate_id == Vote.candidate_id).group_by(Candidate.candidate_name).order_by(db.func.count(Vote.vote_id).desc()).first()
    return q1.Candidate

def get_all_user() -> list:
    return User.query.all()

def get_user(user_id : int) -> User:
    return User.query.filter_by(user_id = user_id).first()

def get_user_division(user_id : int) -> str:
    q = Division.query.join(User, Division.division_id == User.user_id).filter_by(user_id = user_id).first()
    return  q.division_name

def is_user_in_election_team(user_id : int) -> bool:
    q = User.query.filter_by(user_id = user_id).first()
    #tunggu masukin data
    if q.position_id == 1 :
        return True
    else :
        return False


# Add vote to a certain candidate, returns True on success
def add_vote(candidate_id : int, user_id : int) -> bool:
    temp = Vote(user_id = user_id, candidate_id = candidate_id)
    vote = User.query.filter_by(user_id = user_id).first()
    vote.vote = 0
    db.session.add(temp)
    db.session.commit()
    cek = User.query.filter_by(user_id = user_id).first().vote
    if cek == 0 :
        return True
    else :
        return False

def check_password(NIM : str, password : str) -> bool:
    q = User.query.filter_by(NIM = NIM).count()
    if q == 0 :
        return False
    else :
        q = User.query.filter_by(NIM = NIM).first()
        if q.password == password :
            return True
        else :
            return False


