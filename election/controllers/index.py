from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from election.db_helper import add_vote, get_all_candidate, has_suggested, has_voted, insert_suggestion
from election.db import Candidate
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
    WIBTimezone = pytz.timezone('Asia/Jakarta')
    currentDate = datetime.now(WIBTimezone)
    electionDate = datetime(2021, 6, 10)

    # parsedDate = str(datetime.now(WIBTimezone)).split('.')[0]
    print(electionDate)
    all_candidates = get_all_candidate()
    candidate_list = []
    for i in all_candidates:
        candidate_list.append(build_candidate(i))
    return render_template('home.html', 
        username=session["username"], 
        currentTime = currentDate,
        electionDate = str(electionDate),
        candidateList = candidate_list,
        has_suggested = has_suggested(session["user_id"]))
    

@bp.route("/check_candidate")
def check_candidate():
    # Check the time here, give the time to frontend
    WIBTimezone = pytz.timezone('Asia/Jakarta')
    # Render with timer
    print(has_suggested(session["user_id"]))
    return render_template('votes.html', 
        username=session["username"], 
        has_suggested = has_suggested(session["user_id"]))

@bp.route("/vote")
@bp.route("/vote/<int:candidate_id>", methods=["POST", "GET"])
def vote(candidate_id = 0):
    if(request.method == "GET"):
        if(has_voted(session["user_id"])):
            return "waiting for others to vote"
        elif(session["accepted_terms"] is None):
            return redirect(url_for('index.rules'))
        else:
            return render_template('votes_now.html')
    elif(request.method == "POST"):
        if(not candidate_id):
            return redirect(url_for("index.vote"))
        else:
            if(has_voted(session["user_id"])):
                flash("You have already voted.")
            else:
                add_vote(candidate_id, session["user_id"])
                flash("Vote Succesful")
    return redirect(url_for("index.index"))
        
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
            if(len(form) == 6):
                insert_suggestion(form["exman-name-1"], form["exman-division-1"], session["user_id"])
                insert_suggestion(form["exman-name-2"], form["exman-division-2"], session["user_id"])
                insert_suggestion(form["exman-name-3"], form["exman-division-3"], session["user_id"])
                return redirect(url_for("index.index"))
            else:
                flash("Please fill all fields")

@bp.route("/rules", methods=["GET","POST"])
def rules():
    if(request.method == "GET"):
        return render_template('rules.html')
    elif(request.method == "POST"):
        session["accepted_terms"] = True
        return redirect(url_for("index.index"))

def build_candidate(candidate_ref : Candidate) -> dict:
    candidate = {}
    candidate["name"] = candidate_ref.candidate_name
    candidate["id"] = candidate_ref.candidate_id
    return candidate