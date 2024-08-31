import os
from flask import (
    Flask,
    session,
    render_template,
    request,
    abort,
    flash,
    redirect,
    url_for,
)
from passlib.hash import pbkdf2_sha256

app = Flask(__name__)
# Secret key generated with secrets.token_urlsafe()
app.secret_key = "lkaQT-kAb6aIvqWETVcCQ28F-j-rP_PSEaCDdTynkXA"

users = {}


@app.get("/")
def home():
    # session.clear()
    return render_template("home.html", email=session.get("email"))


@app.get("/protected")
def protected():
    if not session.get("email"):
        abort(401)
    return render_template("protected.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    email = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        if pbkdf2_sha256.verify(password, users.get(email)):
            session["email"] = email
            return redirect(url_for("protected"))
        flash("Incorrect e-mail or password.")
    return render_template("login.html", email=email)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        users[email] = pbkdf2_sha256.hash(password)
        # print(users)
        
        flash("Successfully signed up.")
        return redirect(url_for("login"))
        
    return render_template("signup.html")