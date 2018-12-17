from functools import wraps
from flask import session,redirect,url_for,render_template
from models import User
def login_require(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        user = User.query.filter(User.id == user_id).first()
        if user:
            return func(*args, **kwargs)
        else:
            return redirect(url_for("login"))
    return wrapper

@login_require
def index():
    return render_template("index.html")