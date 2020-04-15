from app import db

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

