from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SelectField, FileField
from wtforms.validators import InputRequired, Email, Length


class PlaceForm(FlaskForm):
    title = StringField('Name: ', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    text = StringField('Enter your description: ', validators=[InputRequired(), Length(min=4, max=1000000)])
    area = SelectField("Choose your area: ", choices=[('admiral', "Admiralteyskiy"), ('primorskiy', "Primorskiy")])
    img = FileField('Update Picture', validators=[FileAllowed(['jpg', 'png'])])