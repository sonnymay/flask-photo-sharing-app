# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, URL
from flask_wtf.file import FileAllowed, FileRequired
from flask_login import current_user
from models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ProfileUpdateForm(FlaskForm):
    bio = StringField('Bio', validators=[Length(max=250)])
    location = StringField('Location', validators=[Length(max=100)])
    facebook_link = StringField('Facebook Link', validators=[URL(), Length(max=100)])
    twitter_link = StringField('Twitter Link', validators=[URL(), Length(max=100)])
    instagram_link = StringField('Instagram Link', validators=[URL(), Length(max=100)])
    # Add more fields as needed
    submit = SubmitField('Update Profile')
