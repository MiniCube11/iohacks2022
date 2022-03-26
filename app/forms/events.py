from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, TextAreaField
from wtforms.validators import DataRequired


class AddEventForm(FlaskForm):
    title = StringField('Name', validators=[DataRequired()])
    date = DateField('Event Date', format='%Y-%m-%d', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    is_virtual = BooleanField('Virtual')
    location = StringField('Location')
    website_link = StringField('Link to website', validators=[DataRequired()])
    register_link = StringField('Link to register', validators=[DataRequired()])
    submit = SubmitField('Create Event')
