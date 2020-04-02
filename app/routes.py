from app import application as app
from app import db
from flask import render_template, url_for, redirect, flash
from app.forms import SignUpForm
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Startseite')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm();
    if form.validate_on_submit():
        user = User(vorname=form.vorname.data, nachname=form.nachname.data, telefon=form.telefon.data, email=form.email.data, 
                    plz=form.plz.data, ort=form.ort.data, jersey_size=form.jersey_size.data, jersey_print=form.jersey_print.data)
        flash("Neue Anmeldung: " + str(user))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('signup.html', title='Anmelden', form=form)

@app.route('/admin')
def admin():
    users=User.query.all()
    return render_template('admin.html', title='Chef', users=users)
