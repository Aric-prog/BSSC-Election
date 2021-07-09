from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from election.db_helper import add_vote, get_all_candidate, get_all_user, get_vote_amount_of, has_suggested, has_voted, insert_suggestion, is_user_in_election_team, most_voted_candidate, total_votes, vote_amount
from election.db import Candidate
from election.datetime_handler import get_current_time, get_election_time, result_available, can_vote
from datetime import datetime
import pytz
# Pages included here: 
# - Vote page
# - Exman suggestion page
# - Rules

# TODO : Cache exman suggestion page (array containing all bssc members name)
bp = Blueprint("index", __name__, url_prefix="/")

@bp.before_request
def logged_in():
    if session.get("logged_in") is None:
        return redirect(url_for("user.login"))

@bp.route("/")
def index():
    candidate_list = get_all_candidate_info()
    user_count = len(get_all_user())

    resultAvailable = result_available()
    electionTeam = is_user_in_election_team(session["username"])
    print(get_current_time())
    print(resultAvailable)
    if(not electionTeam):
        if(total_votes() > 0):
            print("goes here")
            resultAvailable = result_available(int((get_vote_amount_of(most_voted_candidate()) / user_count) * 100) >= 66)
            print(resultAvailable)
    else:
        resultAvailable = True
    
    if(resultAvailable):
        return render_template('home.html',
        candidateList = candidate_list,
        electionDate = False,
        has_suggested = has_suggested(session["user_id"]),
        resultAvailable = resultAvailable,
        electionTeam = electionTeam)
    else:
        if(has_voted(session["user_id"])):
            return render_template('home.html',
            candidateList = candidate_list,
            electionDate = "",
            has_suggested = has_suggested(session["user_id"]),
            resultAvailable = resultAvailable,
            electionTeam = electionTeam)
        
        return render_template('home.html',  
            currentTime = get_current_time(),
            electionDate = get_election_time(),
            candidateList = candidate_list,
            has_suggested = has_suggested(session["user_id"]),
            resultAvailable = resultAvailable,
            electionTeam = electionTeam)
    

@bp.route("/check_candidate")
def check_candidate():
    # Check the time here, give the time to frontend
    candidate_list = get_all_candidate_info()
    return render_template('votes.html', 
        username=session["username"], 
        has_suggested = has_suggested(session["user_id"]),
        candidateList = candidate_list,
        canVote = can_vote())

@bp.route("/vote")
@bp.route("/vote/<int:candidate_id>", methods=["POST", "GET"])
def vote(candidate_id = 0):
    if(request.method == "GET"):
        if(has_voted(session["user_id"])):
            return redirect(url_for('index.index'))
        else:
            candidate_list = get_all_candidate_info()
            if(session["accepted_terms"] is None):
                return redirect(url_for('index.rules'))
            else:
                return render_template('votes_now.html', candidateList = candidate_list, canVote = can_vote())
    elif(request.method == "POST"):
        if(not candidate_id):
            return (url_for("index.vote"))
        else:
            if(not has_voted(session["user_id"])):
                add_vote(candidate_id, session["user_id"])
                # Return url for succesful vote
                return (url_for('index.index'))
            # Redirect to page with, waiting for others to vote
        return (url_for("index.index"))
                
        
@bp.route("/exman_suggestion", methods=["GET", "POST"])
def exman_suggestion():
    if(request.method == "GET"):
        suggested = has_suggested(session["user_id"])
        if(suggested):
            return redirect(url_for("index.index"))
        return render_template('Exman_suggestion.html')
    elif(request.method == "POST"):
        # Check if user has suggested or not from database i guess
        suggested = has_suggested(session["user_id"])
        if(suggested):
            return redirect(url_for("index.index"))
        else:
            # Insert suggestion into db
            form = request.form
            print(form)
            for i in range(len(form) // 2):
                iteration = str(i + 1)
                if(form.get("exman-name-" + iteration) and form.get("exman-division-" + iteration)):
                    insert_suggestion(form["exman-name-" + iteration], form["exman-division-" + iteration], session["user_id"])
                
            return redirect(url_for("index.index"))

@bp.route("/rules", methods=["GET","POST"])
def rules():
    if(request.method == "GET"):
        return render_template('rules.html')
    elif(request.method == "POST"):
        session["accepted_terms"] = True
        return redirect(url_for("index.vote"))

def build_candidate(candidate_ref : Candidate) -> dict:
    candidate = {}
    candidate["name"] = candidate_ref.candidate_name
    candidate["id"] = candidate_ref.candidate_id
    candidate["imagepath"] = candidate_ref.candidate_name.replace(' ','-') + '.webp'
    return candidate

def get_all_candidate_info() -> list:
    all_candidates = get_all_candidate()
    candidate_list = []
    for i in all_candidates:
        candidate_list.append(build_candidate(i))
    return candidate_list