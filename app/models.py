from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vorname = db.Column(db.String(64), index=True)
    nachname = db.Column(db.String(64), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    telefon = db.Column(db.String(10), index=True, unique=True)
    plz = db.Column(db.String(10), index=True)
    ort = db.Column(db.String(60), index=True)
    jersey_size = db.Column(db.String(10), index=True)
    jersey_print = db.Column(db.String(10), index=True)

    def __repr__(self):
        return '<Player {} {}>'.format(self.vorname, self.nachname)


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Admin {}>'.format(self.username)

# Flask-Login needs to know how to load an admin-user from the db
@login.user_loader
def load_user(id):
    return Admin.query.get(int(id))





