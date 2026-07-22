from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from auth.models import User
from extensions import db

auth_bp = Blueprint("auth", __name__)


# ---------------- HOME ----------------
@auth_bp.route("/")
def home():
    return redirect(url_for("auth.signup"))


# ---------------- SIGN UP ----------------
@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        # Debug (baad mein delete kar dena)
        print("Full Name:", full_name)
        print("Username :", username)
        print("Email    :", email)
        print("Password :", password)

        # Check Email
        if User.query.filter_by(email=email).first():
            return "Email already exists"

        # Check Username
        if User.query.filter_by(username=username).first():
            return "Username already exists"

        # Create User
        new_user = User(
            full_name=full_name,
            username=username,
            email=email,
            password=generate_password_hash(password)
        )

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("auth.signin"))

    return render_template("signup.html")


# ---------------- SIGN IN ----------------
@auth_bp.route("/signin", methods=["GET", "POST"])
def signin():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user is None:
            return "Email not found"

        if not check_password_hash(user.password, password):
            return "Invalid password"

        return "Login Successful"

    return render_template("signin.html")