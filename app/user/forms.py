from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import Length


class RegistrationForm(FlaskForm):
    username = StringField("Username", [Length(min=4, max=25)])
    password = PasswordField("Password", [Length(min=4, max=25)])


class LoginForm(FlaskForm):
    username = StringField("Username", [Length(min=4, max=25)])
    password = PasswordField("Password", [Length(min=4, max=25)])
    remember = BooleanField("Remember Me")
