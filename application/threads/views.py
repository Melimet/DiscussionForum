from flask import render_template, request, redirect, url_for

from application import app, db
from application.threads.thread import thread
from application.threads.forms import ThreadForm


@app.route("/threads/new/")
def threads_form():
    return render_template("threads/new.html", form=ThreadForm())


##Create a new thread
@app.route("/threads/", methods=["POST"])
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form = form)


##If the name of the thread is left empty, it will use the comment instead as title
##If the lenght of name string is over 50 when taking it from comment, the lenght will be reduced to 50

    name = request.form.get("name")
    if len(request.form.get("name")) == 0:
        name = request.form.get("comment")
        name = name[:50]

    t = thread(name, request.form.get("comment"))

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
