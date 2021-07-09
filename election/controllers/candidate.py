from election.datetime_handler import result_available
from election.db_helper import get_all_candidate, get_all_user, get_candidate, get_vote_amount_of, has_asked_question, insert_question, is_user_in_election_team, most_voted_candidate, total_votes
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
        if(form.get("subject")):
            insert_question(form["subject"], form["question"], candidate_id, session["user_id"])
        return redirect(url_for('candidate.blueprint', candidate_id=candidate_id))

@bp.route("/result")
def result():
    # Calculate the highest vote
    # Give the data to the html and js
    voteAmount = total_votes()
    user_count = len(get_all_user())
    aboveSixtySixPercent = False
    if(voteAmount > 0):
        aboveSixtySixPercent = int((get_vote_amount_of(most_voted_candidate()) / user_count) * 100) >= 66
        print("above sixty ", aboveSixtySixPercent)
    if(voteAmount > 0 and (aboveSixtySixPercent or is_user_in_election_team(session["username"]))):
        winnerCandidate = most_voted_candidate()
        
        winner = {}
        winner["name"] = winnerCandidate.candidate_name
        winner["imagepath"] = winnerCandidate.candidate_name.replace(" ", "_")
        
        candidateList = []
        candidateRefList = get_all_candidate()
        
        userCount = len(get_all_user())
        barCount = int(math.ceil(userCount / 100.0)) * 100
        
        noVotePercentage = round(((userCount - voteAmount) / userCount) * 100)
        votePercentage = 100 - noVotePercentage
        
        prevHighestVote = 0
        for c in candidateRefList:
            candidate = {}
            candidate["name"] = c.candidate_name
            candidate["imagepath"] = c.candidate_name.replace(" ", "-")
            candidate["votes"] = get_vote_amount_of(c)
            if(candidate["votes"] > prevHighestVote):
                prevHighestVote = candidate["votes"]
            candidateList.append(candidate)

        return render_template('result.html', 
            winner=winner, 
            candidateList = candidateList, 
            totalVotes = voteAmount, 
            userCount = userCount,
            barCount = barCount,
            votePercentage = votePercentage,
            noVotePercentage = noVotePercentage,
            aboveSixtySixPercent = aboveSixtySixPercent)
    else:
        return redirect(url_for('index.index'))