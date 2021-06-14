from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, URL

class MoodForm(FlaskForm):
    """Form for inputting a mood"""
    # Mood as input
    mood = StringField('Mood', validators=[DataRequired()])
    submit = SubmitField('Submit')