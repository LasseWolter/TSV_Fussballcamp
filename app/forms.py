from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Email, ValidationError, Length
from app.models import User

class SignUpForm(FlaskForm):
    vorname = StringField('Vorname', validators=[DataRequired()])
    nachname = StringField('Nachname', validators=[DataRequired()])
    email= StringField('Email', validators=[DataRequired(), Email()])
    telefon=StringField('Telefon', validators=[DataRequired()])
    plz=StringField('Postleitzahl',validators=[DataRequired()])
    ort=StringField('Wohnort', validators=[DataRequired()]) 
    jersey_size=SelectField('Trikot-Größe',choices=[('128','128'), ('164','164'), ('176','176')], validators=[DataRequired()])
    jersey_print=StringField('Trikot-Aufdruck',validators=[DataRequired(), Length(max=10)])
    submit = SubmitField('Anmelden')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is already in use.')

    def validate_telefon(self, telefon):
        try:
            int(telefon.data)
        except ValueError:
            raise ValidationError('This is not a valid phone number.')
        user = User.query.filter_by(telefon=telefon.data).first()
        if user is not None:
            raise ValidationError('This telefon number is already in use.')

    def validate_plz(self, plz):
        try:
            int(plz.data)
        except ValueError:
            raise ValidationError('This is not a valid plz.')
