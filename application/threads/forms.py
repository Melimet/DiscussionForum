from flask_wtf import FlaskForm
from wtforms import *

class ThreadForm(FlaskForm):
    name = StringField("Thread name", [validators.Length(max=50)])
    comment = StringField("Comment", [validators.Length(min=1, max=500)])

    class Meta:
        csrf = False