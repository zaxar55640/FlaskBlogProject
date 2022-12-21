from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class RegisterForm(FlaskForm):
    email = StringField('Enter your Email:', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    name = StringField('Enter your Username: ', validators=[InputRequired(), Length(min=4, max=30)])
    password = PasswordField('Enter your password:', validators=[InputRequired(), Length(min=4, max=80)])