from flask_wtf import FlaskForm
from wtforms import *

class ReplyForm(FlaskForm):
    reply = StringField("Reply", [validators.Length(min=1, max=500)])

    class Meta:
        csrf = False