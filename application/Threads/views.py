from application import app, db
from flask import render_template, request, redirect, url_for
from application.Threads.Thread import Thread


@app.route("/Threads/new/")
def Threads_form():
    return render_template("Threads/new.html")


##Create a new Thread
@app.route("/Threads/", methods=["POST"])
def Threads_create():
    t = Thread(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("Threads_index"))


@app.route("/Threads", methods=["GET"])
def Threads_index():
    return render_template("Threads/list.html", Threads=Thread.query.all())


@app.route("/Thread/<Thread_id>/", methods=["POST"])
def Thread_vote(Thread_id):
    t = Thread.query.get(Thread_id)
    t.votes += 1
    db.session().commit()

    return redirect(url_for("Threads_index"))
