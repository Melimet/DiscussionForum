from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.threads.models import thread
from application.threads.forms import ThreadForm

from application.replies.models import reply
from application.replies.forms import ReplyForm

from application.auth.models import User


@app.route("/threads/new/")
def threads_form():
    return render_template("threads/new.html", form=ThreadForm())


##Create a new thread
@app.route("/threads/", methods=["POST"])
@login_required
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form=form)

    ##If the name of the thread is left empty, it will use the comment instead as title
    ##If the lenght of name string is over 50 when taking it from comment, the lenght will be reduced to 50

    name = request.form.get("name")
    if len(request.form.get("name")) == 0:
        name = request.form.get("comment")
        name = name[:50]

    t = thread(name, request.form.get("comment"))
    t.account_id = current_user.id

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads=thread.query.all(), users=User.query.all(),
                           replies=reply.query.all(), form=ReplyForm())


@app.route("/thread/<thread_id>/", methods=["POST"])
@login_required
def thread_vote(thread_id):
    t = thread.query.get(thread_id)
    t.votes += 1
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/remove/<thread_id>/", methods=["POST"])
@login_required
def thread_remove(thread_id):
    t = thread.query.get(thread_id)

    db.session().delete(t)
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/<thread_id>", methods=["POST"])
@login_required
def reply_add(thread_id):

    form = ReplyForm(request.form)

    if not form.validate():
        return redirect(url_for("threads_index"))
        ##render_template("threads/list.html", form=form)

    r = reply(form.reply.data)
    r.account_id = current_user.id
    r.thread_id = thread_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("threads_index"))
