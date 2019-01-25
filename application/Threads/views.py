from application import app, db
from flask import render_template, request, redirect, url_for
from application.Threads.Thread import Thread

@app.route("/Threads/new/")
def Threads_form():
    return render_template("Threads/new.html")

@app.route("/Threads/", methods=["POST"])
def Threads_create():

    t = Thread(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("Threads_index"))

@app.route("/Threads", methods=["GET"])
def Threads_index():
    return render_template("Threads/list.html", Threads = Thread.query.all())
