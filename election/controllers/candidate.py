from election.db_helper import get_candidate, insert_question
from flask import Blueprint, render_template, session, redirect, url_for, request

# Pages included here : 
# - Blueprint page
# - Result

bp = Blueprint("candidate", __name__, url_prefix="/candidate")

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
        candidate["visi"] = candidate_ref.candidate_vision
        candidate["misi"] = candidate_ref.candidate_mission
        candidate["video_link"] = candidate_ref.candidate_video
        candidate["drive_link"] = candidate_ref.candidate_blueprint

        return render_template('blueprint.html', candidate)
    elif(request.method == "POST"):
        # Post questions
        form = request.form
        insert_question(form["subject"], form["question"], candidate_id, session["user_id"])
        
    return "blueprint"

@bp.route("/result")
def result():
    # Calculate the highest vote
    # Give the data to the html and js
    return render_template('result.html')