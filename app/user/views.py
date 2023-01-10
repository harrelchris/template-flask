from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from .crypto import hash_password, validate_password
from .forms import LoginForm, RegistrationForm
from .models import User


def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        exists = User.where(username=form.username.data).first()
        if exists:
            flash("Username unavailable", category="error")
            return render_template("user/register.html", form=form)
        password = hash_password(form.password.data)
        user = User(
            username=form.username.data,
            password=password,
        )
        user.save()
        flash("Account created", category="success")
        return redirect(url_for("user.login"))
    return render_template("user/register.html", form=form)


def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.where(username=form.username.data).first()
        if validate_password(form.password.data, user.password):
            login_user(user=user, remember=form.remember.data)
            flash(f"Logged in as {user.username}", category="success")
            # TODO: handle next - https://web.archive.org/web/20120517003641/http://flask.pocoo.org/snippets/62/
            return redirect(url_for("public.index"))
        flash("Invalid password", category="error")
    return render_template("user/login.html", form=form)


@login_required
def logout():
    logout_user()
    flash("Logged out", category="success")
    return redirect(url_for("public.index"))
