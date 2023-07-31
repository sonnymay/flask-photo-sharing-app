# models.py

from main import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    bio = db.Column(db.String(250))
    location = db.Column(db.String(100))
    facebook_link = db.Column(db.String(100))
    twitter_link = db.Column(db.String(100))
    instagram_link = db.Column(db.String(100))
    # Add more fields as needed

# Rest of the code remains the same
