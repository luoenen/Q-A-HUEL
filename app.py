from flask import Flask, redirect, render_template, url_for, request, session
import config
from exts import db
from models import User,Question,Comment
from decorators import login_require
from sqlalchemy import or_
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def hello_world():
    return redirect(url_for("index"))


@app.route("/index")
def index():
    context = {
        "questions": Question.query.order_by("time").all()
    }
    return render_template("index.html",**context)
@app.route("/register", methods=["GET","POST"])
def register():
    methods = request.method
    if methods == "GET":
        return render_template("register.html")
    else:
        account = request.form.get("account")
        name = request.form.get("name")
        tel = request.form.get("tel")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if password1 != password2:
            return "密码不一致"
        find_user = User.query.filter(User.account == account).first()
        if find_user:
            return "该学号已经注册"
        create_user = User(account=account, name=name, tel=tel, password=password1)
        db.session.add(create_user)
        db.session.commit()
        return "注册成功"

@app.route("/login", methods=["GET","POST"])
def login():
    methods = request.method
    if methods == "GET":
        return render_template("login.html")
    else:
        account = request.form.get("account")
        password = request.form.get("password")
        user = User.query.filter(User.account == account, User.password == password).first()
        if user:
            session["user_id"] = user.id
            session.permanent = True
            return redirect(url_for("index"))
        else:
            return "账号密码错误"

@app.context_processor
def context():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {"user": user}
        else:
            return {}
    return {}

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@app.route("/information")
def information():
    user_id = session.get("user_id")
    user = User.query.filter(User.id == user_id).first()
    return render_template("information.html", information= str("ID:"+str(user.id)+"\n"+"Account:"+str(user.account)+"Name:"+str(user.name)+"Password:"+str(user.password)))

@app.route("/question",methods=["POST","GET"])
@login_require
def question():
    methods = request.method
    if methods == "GET":
        return render_template("question.html")
    else:
        user_id = session.get("user_id")
        user = User.query.filter(User.id == user_id).first()
        if user:
            sort = request.form.get("type")
            title = request.form.get("title")
            content = request.form.get("context")
            questions = Question(type=sort, title=title, context=content)
            user_id = session.get("user_id")
            user = User.query.filter(User.id == user_id).first()
            question.author = user
            db.session.add(questions)
            db.session.commit()
            return redirect(url_for("index"))

@app.route("/detail/<question_id>")
def detail(question_id):
    question = Question.query.filter(Question.id == question_id ).first()
    return render_template("detail.html",question_model = question)

@app.route("/comment",methods=["post"])
@login_require
def comment():
    comment = request.form.get("comment")
    question_id = request.form.get("id")
    answer = Comment(comment = comment)

    user_id = session.get("user_id")
    user = User.query.filter(User.id == user_id).first()
    question = Question.query.filter(Question.id == question_id).first()
    answer.author = user
    answer.question = question
    db.session.add(answer)
    db.session.commit()
    return redirect(url_for("detail",question_id=question_id))

@app.route("/search",methods=["get","post"])
def search():
    q = request.form.get("search")
    questions = Question.query.filter(or_(Question.title.contains(q), Question.context.contains(q))).order_by("-time")
    return render_template("index.html",questions=questions)


if __name__ == '__main__':
    app.run(port=8081)
