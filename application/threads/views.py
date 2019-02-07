from application import app, db
from flask import render_template, request, redirect, url_for
from application.threads.thread import thread


@app.route("/threads/new/")
def threads_form():
    return render_template("threads/new.html")


##Create a new thread
@app.route("/threads/", methods=["POST"])
def threads_create():
    t = thread(request.form.get("name"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads=thread.query.all())


@app.route("/thread/<thread_id>/", methods=["POST"])
def thread_vote(thread_id):
    t = thread.query.get(thread_id)
    t.votes += 1
    db.session().commit()

    return redirect(url_for("threads_index"))
