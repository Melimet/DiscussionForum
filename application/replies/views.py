from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.replies.forms import ReplyForm
from application.replies.models import reply


##Doesn't actually do anything
##Unused
@app.route("/threads/<thread_id>/", methods=["POST"])
@login_required
def reply_add(thread_id):

    form = ReplyForm(request.form)

    if not form.validate():
        return render_template("threads/list.html", form = form)

    r = reply(form.reply.data)
    r.account_id = current_user.id
    r.thread_id = thread_id

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("threads/<thread_id>/"))