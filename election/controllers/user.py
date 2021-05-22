from election.db import User
from flask import Blueprint, render_template, session, redirect, url_for, request
from election.db_helper import check_password, get_user_division, get_user_from_NIM, get_user_position, vote_amount

# Pages included here :
#  - User profile
#  - Election team profile
#  - Login

bp = Blueprint("user", __name__, url_prefix="/")

@bp.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "GET"):
        return render_template('login.html')
    elif(request.method == "POST"):
        
        form = request.form
        NIM = form["NIM"]
        password = form["password"]
        
        # Validate nim and password here
        # Database request here
        validated = check_password(NIM, password)
        if(validated):
            # Data saved here
            user = get_user_from_NIM(NIM)
            
            session["division"] = get_user_division(user.user_id)
            session["position"] = get_user_position(user.user_id)

            session["email"] = user.email
            session["user_id"] = user.user_id
            session["POB"] = user.POB
            session["DOB"] = user.DOB
            
            session["logged_in"] = True
            session["username"] = user.name
            session["NIM"] = form["NIM"]
            
            return redirect(url_for("index.index"))
        else:
            # Render template login with argument, hasFailed
            # Highlight input box with red
            return render_template('login.html', errorMessage="NIM or Password not valid")

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.login"))

@bp.route("/profile")
def profile():
    # TODO : Instantiate and cache election team nim list
    electionTeamNIMList = []
    if(session.get("NIM") in electionTeamNIMList):
        return "election team profile"
    else:
        print(session["user_id"])
        return render_template('profile.html', user = session.get("user_ref"), vote_left = vote_amount(session["user_id"]))