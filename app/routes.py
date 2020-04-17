from app import application as app
from app import db
from flask import render_template, url_for, redirect, flash, request
from app.forms import SignUpForm, AdminLoginForm
from app.models import Player, Admin
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Startseite')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm();
    if form.validate_on_submit():
        player = Player(vorname=form.vorname.data, nachname=form.nachname.data, telefon=form.telefon.data, email=form.email.data,
                    plz=form.plz.data, ort=form.ort.data, jersey_size=form.jersey_size.data, jersey_print=form.jersey_print.data)
        flash("Neue Anmeldung: " + str(player))
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', title='Anmelden', form=form)

@app.route('/admin')
@login_required
def admin():
    players=Player.query.all()
    return render_template('admin.html', title='Chef', players=players)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = AdminLoginForm()
    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Falscher Benutzername oder falsches Passwort")
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        # The second part prevents from redirecting to some foreign webpage
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Admin Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))