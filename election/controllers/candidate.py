from flask import Blueprint, render_template, session, redirect, url_for, request

# Pages included here : 
# - Blueprint page
# - Candidate list page
# - Result

bp = Blueprint("candidate", __name__, url_prefix="/candidate")

@bp.before_request
def logged_in():
    if not session.get("logged_in"):
        redirect(url_for("user.login"))

@bp.route("/blueprint/<int:candidate_id>", methods=["GET", "POST"])
def blueprint():
    # Query from database visi misi from candidate id
    # Get video link and display it
    return "blueprint"