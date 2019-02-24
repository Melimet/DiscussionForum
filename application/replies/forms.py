from flask_wtf import FlaskForm
from wtforms import *

class ReplyForm(FlaskForm):
    reply = TextAreaField("",[validators.Length(min=1, max=500)])

    class Meta:
        csrf = False