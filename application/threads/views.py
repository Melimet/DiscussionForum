from application import app, db, login_required, login_manager

from flask import render_template, request, redirect, url_for
from flask_login import current_user

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
@login_required(role="ANY")
def threads_create():
    form = ThreadForm(request.form)

    if not form.validate():
        return render_template("threads/new.html", form=form)

    ##If the name of the thread is left empty, it will use the comment instead as title
    ##If the lenght of name string is over 50 when taking it from comment, the lenght will be reduced to 50

    name = request.form.get("name")
    if len(request.form.get("name")) == 0:
        name = request.form.get("comment")[:50]

    threadNew = thread(name, request.form.get("comment"))
    threadNew.account_id = current_user.id

    db.session().add(threadNew)
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/threads", methods=["GET"])
def threads_index():
    return render_template("threads/list.html", threads=thread.query.all(), users=User.query.all(),
                           replies=reply.query.all(), form=ReplyForm())


@app.route("/thread/<thread_id>/", methods=["POST"])
@login_required(role="ANY")
def thread_vote(thread_id):
    t = thread.query.get(thread_id)
    t.votes += 1
    db.session().commit()

    return redirect(url_for("threads_index"))


@app.route("/remove/<thread_id>/", methods=["POST"])
@login_required(role="ANY")
def thread_remove(thread_id):
    threadRemove = thread.query.get(thread_id)
    ##Get replies to be deleted

    repliesRemove = reply.__table__.delete().where(reply.thread_id == thread_id)

    if threadRemove.account_id == current_user.id or current_user.ADMIN:
        db.session.execute(repliesRemove)
        db.session().delete(threadRemove)
        db.session().commit()
        return redirect(url_for("threads_index"))

    return login_manager.unauthorized()


@app.route("/<thread_id>", methods=["POST"])
@login_required(role="ANY")
def reply_add(thread_id):
    form = ReplyForm(request.form)

    if not form.validate():
        return redirect(url_for("threads_index"))
        ##render_template("threads/list.html", form=form)

    replyAdd = reply(form.reply.data)
    replyAdd.account_id = current_user.id
    replyAdd.thread_id = thread_id

    db.session().add(replyAdd)
    db.session().commit()

    return redirect(url_for("threads_index"))
