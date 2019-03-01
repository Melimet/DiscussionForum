from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required, login_manager
from application.auth.models import User
from application.auth.forms import LoginForm, RegistrationForm, EmailChangeForm, PasswordChangeForm


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form=form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()

    if not user:
        return render_template("auth/loginform.html", form=form, error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/logout")
@login_required(role="ANY")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/auth/new", methods=["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/new.html", form=RegistrationForm())

    form = RegistrationForm(request.form)



    if not form.validate():
        return render_template("auth/new.html", form=form)

    ##Checking if a user with the username already exists
    userNew = User.query.filter_by(username = form.username.data).first()
    if userNew:
        return render_template("auth/new.html", form=form, errorMessage="Username has already been registered.")

    userNew = User(form.username.data, form.email.data, form.password.data)

    db.session.add(userNew)
    db.session.commit()

    return redirect(url_for("index"))

@app.route("/auth/profile", methods=["GET"])
def auth_profileGet():
    formEmail = EmailChangeForm()
    formPassword = PasswordChangeForm()

    return render_template("auth/profile.html", formEmail=formEmail, formPassword=formPassword)


@app.route("/auth/profile/<id>", methods=["POST"])
@login_required(role="ANY")
def auth_profile(id):

    formEmail = EmailChangeForm(request.form)
    formPassword = PasswordChangeForm(request.form)


    if formEmail.submit1.data and formEmail.validate():

        user = db.session.query(User).filter(User.id == id).first()

        user.email = formEmail.email.data
        db.session.commit()
        return redirect(url_for("auth_profileGet"))


    if formPassword.submit2.data and formPassword.validate():

        user = db.session.query(User).filter(User.id == id).first()
        user.password = formPassword.password.data
        db.session.commit()
        return redirect(url_for("auth_profileGet"))

    return render_template("auth/profile.html", formEmail=formEmail, formPassword=formPassword)
