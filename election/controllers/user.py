from election.db import User, Question
from flask import Blueprint, render_template, session, redirect, url_for, request
from election.db_helper import check_password, get_all_question, get_candidate_from, get_user, get_user_division, get_user_from_NIM, get_user_position, is_user_in_election_team, vote_amount

# Pages included here :
#  - User profile
#  - Election team profile
#  - Login

bp = Blueprint("user", __name__, url_prefix="/election")

@bp.route("/login", methods=["GET","POST"])
def login():
    if(request.method == "GET"):
        if not session.get("logged_in") is None:
            return redirect(url_for("index.index"))
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
            user_ref = get_user_from_NIM(NIM)
            user = build_user_dict_from(user_ref)
            
            session["logged_in"] = True
            session["username"] = user_ref.name
            session["user_id"] = user_ref.user_id
            session["accepted_terms"] = None
            
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
    user = build_user_dict_from(get_user(session["user_id"]))
    questionList = []
    if(is_user_in_election_team(session["user_id"])):
        all_questions = get_all_question()
        for i in all_questions:
            questionList.append(build_question(i))
        return render_template('profile.html', user = user, vote_left = vote_amount(session["user_id"]), question_list = questionList)
    else:
        print(session["user_id"])
        return render_template('profile.html', user = user, vote_left = vote_amount(session["user_id"]))

def build_user_dict_from(user_ref : User) -> dict:
    user = {}
    user["division"] = get_user_division(user_ref.user_id)
    user["position"] = get_user_position(user_ref.user_id)

    user["email"] = user_ref.email
    user["POB"] = user_ref.POB
    user["DOB"] = user_ref.DOB
    
    user["NIM"] = user_ref.NIM
    return user

def build_question(question_ref : Question) -> dict:
    question = {}
    question["subject"] = question_ref.question_subject
    question["body"] = question_ref.question_body
    # question["for_candidate"] = get_candidate_from(question_ref).candidate_name

    return question