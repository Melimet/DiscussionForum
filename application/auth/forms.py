from flask_wtf import FlaskForm
from wtforms import *

class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3, max=20)])
    password = PasswordField("Password", [validators.Length(min=6, max=20)])

    class Meta:
        csrf = False

class RegistrationForm(FlaskForm):
    email = StringField("Email", [validators.Length(min=5, max=50), validators.Email(message="Please make sure your email address is valid")])
    username = StringField("Username", [validators.Length(min=3, max=20)])
    password = PasswordField("Password", [validators.Length(min=6, max=20)])

    class Meta:
        csrf = False

class EmailChangeForm(FlaskForm):
    email = StringField("email", [validators.Length(min=5, max=50), validators.Email(message="Please make sure your email address is valid")])
    submit1 = SubmitField('Update email')

    class Meta:
        csrf = False

class PasswordChangeForm(FlaskForm):

    password = PasswordField("password", [validators.Length(min=6, max=20)])
    submit2 = SubmitField('Update password')

    class Meta:
        csrf = False