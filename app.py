from flask import Flask, render_template, url_for, request, redirect, flash
from datetime import datetime
from forms import MyForm
from flask_sqlalchemy import SQLAlchemy
import os
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = '\x13\x15\xf3]\xc7\x96e4&\xc8\x89\xe7\xc4\xc7\xbd\x8dwmv0\xa6'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['DEBUG'] = True
db = SQLAlchemy(app)
import models

toolbar = DebugToolbarExtension(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = MyForm()
    users = models.User.get_all()
    if form.validate_on_submit:
        username = form.username.data
        email = form.email.data
        if username and email:
            user = models.User(username=username, email=email)
            db.session.add(user)
            db.session.commit()
            flash("Stored '{}'".format(username))
            return redirect(url_for('index'))
    return render_template('main/index.html', form=form, users=users)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@app.errorhandler(500)
def server_error(e):
    return render_template('errors/500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
