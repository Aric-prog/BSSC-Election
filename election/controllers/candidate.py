from election.db_helper import get_all_candidate, get_all_user, get_candidate, get_vote_amount_of, has_asked_question, insert_question, most_voted_candidate, total_votes
from flask import Blueprint, render_template, session, redirect, url_for, request
import math
# Pages included here : 
# - Blueprint page
# - Result

bp = Blueprint("candidate", __name__, url_prefix="/")

@bp.before_request
def logged_in():
    if not session.get("logged_in"):
        redirect(url_for("user.login"))

@bp.route("/blueprint/<int:candidate_id>", methods=["GET", "POST"])
def blueprint(candidate_id):
    if(request.method == "GET"):
        # Query from database visi misi from candidate id
        # Get video link and display it
        candidate = {}
        candidate_ref = get_candidate(candidate_id)

        candidate["name"] = candidate_ref.candidate_name
        candidate["imagepath"] = candidate_ref.candidate_name.replace(' ','-') + '.webp'
        candidate["vision"] = candidate_ref.candidate_vision
        candidate["mission"] = candidate_ref.candidate_mission
        candidate["video_link"] = candidate_ref.candidate_video
        candidate["drive_link"] = candidate_ref.candidate_blueprint

        return render_template('blueprint.html', candidate = candidate, has_asked = has_asked_question(session["user_id"]), candidate_id = candidate_id)
    elif(request.method == "POST"):
        # Post questions
        form = request.form
        if(not has_asked_question):
            insert_question(form["subject"], form["question"], candidate_id, session["user_id"])
        return redirect(url_for('index.vote'))

@bp.route("/result")
def result():
    # Calculate the highest vote
    # Give the data to the html and js
    voteAmount = total_votes()
    # print(voteAmount)
    
    winnerCandidate = most_voted_candidate()
    if(winnerCandidate is None):
        return redirect(url_for('index.index'))
    
    winner = {}
    winner["name"] = winnerCandidate.candidate_name
    
    candidateList = []
    candidateRefList = get_all_candidate()
    
    userCount = len(get_all_user())
    barCount = int(math.ceil(userCount / 100.0)) * 100
    print(barCount)
    noVotePercentage = round(((userCount - voteAmount) / userCount) * 100)
    votePercentage = 100 - noVotePercentage
    for c in candidateRefList:
        candidate = {}
        candidate["name"] = c.candidate_name
        candidate["votes"] = get_vote_amount_of(c)
        candidateList.append(candidate)
        
    return render_template('result.html', 
        winner=winner, 
        candidateList = candidateList, 
        totalVotes = voteAmount, 
        userCount = userCount,
        barCount = barCount,
        votePercentage = votePercentage,
        noVotePercentage = noVotePercentage)