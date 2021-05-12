from flask import Blueprint, render_template, session, redirect, url_for, request

# Pages included here :
#  - User profile
#  - Election team profile
#  - Login

bp = Blueprint("user", __name__, url_prefix="/")

@bp.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "GET"):
        return "login"
    elif(request.method == "POST"):
        
        form = request.form
    
        # Validate nim and password here
        # Database request here
        # if(form["NIM"] == "nim from database" and form["password"] == "pass from database"):
        #     validated = True
        # else:
        #     validated = False
        
        validated = True

        if(validated):
            # Data saved here
            session["logged_in"] = True
            session["username"] = "Aric"
            session["NIM"] = form["NIM"]
            
            return redirect(url_for("index.index"))
        else:
            # Render template login with argument, hasFailed
            # Highlight input box with red
            return "login, but failed"

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
        return "normal profile"