from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import Player 

class SignUpForm(FlaskForm):
    firstname = StringField('Vorname', validators=[DataRequired()])
    lastname = StringField('Nachname', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    phone=StringField('Telefon', validators=[DataRequired()])
    plz=StringField('Postleitzahl',validators=[DataRequired()])
    city=StringField('Wohnort', validators=[DataRequired()])
    jersey_size=SelectField('Trikot-Größe',choices=[('128','128'), ('164','164'), ('176','176')], validators=[DataRequired()])
    jersey_print=StringField('Trikot-Aufdruck',validators=[DataRequired(), Length(max=10)])
    comment= TextAreaField('Anmerkungen')
    submit = SubmitField('Anmelden')
    
    def validate_email(self, email):
        player = Player.query.filter_by(email=email.data).first()
        if player is not None:
            raise ValidationError('This email is already in use.')

    def validate_phone(self, phone):
        try:
            int(phone.data)
        except ValueError:
            raise ValidationError('This is not a valid phone number.')
        player = Player.query.filter_by(phone=phone.data).first()
        if player is not None:
            raise ValidationError('This telefon number is already in use.')

    def validate_plz(self, plz):
        try:
            int(plz.data)
        except ValueError:
            raise ValidationError('This is not a valid plz.')

class AdminLoginForm(FlaskForm):
    username = StringField('Benutzername', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Einloggen')