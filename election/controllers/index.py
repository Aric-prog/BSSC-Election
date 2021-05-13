from flask import Blueprint, render_template, session, redirect, url_for, request

# Pages included here: 
# - Vote page
# - Exman suggestion page
# - Rules

# TODO : Cache exman suggestion page (array containing all bssc members name)

bp = Blueprint("index", __name__, url_prefix="/")

@bp.before_request
def logged_in():
    if not session.get("logged_in"):
        redirect(url_for("user.login"))

    # This is to check if the user has accepted terms or not
    # elif not session.get("accepted_terms") and UserId exist in suggestion:
    #     redirect(url_for('index.rules'))

# For now this is used for testing pages
@bp.route("/")
def index():
    return render_template('profile.html', username="contoh nama")

@bp.route("/vote/<int:candidate_id>", methods=["POST", "GET"])
def vote(candidate_id):
    if(request.method == "GET"):
        pass
    elif(request.method == "POST"):
        # if(not db.has_voted(session.get("ID"))):
        # Make database request to add vote
        pass

    return redirect(url_for("index.index"))

@bp.route("/exman_suggestion", methods=["GET", "POST"])
def exman_suggestion():
    if(request.method == "GET"):
        return "exman_suggestion"    
    elif(request.method == "POST"):
        # Check if user has suggested or not from database i guess
        has_suggested = False
        if(has_suggested):
            return redirect(url_for("index.index"))
        else:
            form = request.form
            for key,value in form.items():
                # Insert key and value into exman suggestion
                # Insert value hasSuggested into database
                ""
            return redirect("index.rules")

@bp.route("/rules", methods=["GET","POST"])
def rules():
    if(request.method == "GET"):
        return "show rules here"
    elif(request.method == "POST"):
        session["accepted_terms"] = True
        return redirect(url_for("index.index"))