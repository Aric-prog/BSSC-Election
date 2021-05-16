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
    pass

# Returns the remaining vote for a user
def vote_amount(user_id : int) -> int:
    return User.query.filter_by(user_id = user_id).first().vote
 
def get_all_candidate() -> list:
    return Candidate.query.all()

def get_candidate(candidate_id : int) -> Candidate:
    return Candidate.query.filter_by(candidate_id = candidate_id).first()

# Returns the total amount of votes
def total_votes() -> int:
    pass

def most_voted_candidate() -> Candidate:
    pass

def get_all_user() -> list:
    return User.query.all()

def get_user(user_id : int) -> User:
    User.query.filter_by(user_id = user_id).first()

def get_user_division(user_id : int) -> str:
    pass

def is_user_in_election_team(user_id : int) -> bool:
    pass

# Add vote to a certain candidate, returns True on success
def add_vote(candidate_id : int) -> bool:
    pass

def check_password(NIM : str, password : str) -> bool:
    pass


