from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()


class Course(db.Model, SerializerMixin):
    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    thumbnail = db.Column(db.Text, nullable=True)  # Stores Base64 image
    description = db.Column(db.Text, nullable=True)
    duration = db.Column(db.Integer, nullable=True)  # Duration in hours
    owner = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(50), nullable=True)  # e.g., active, inactive
    # Beginner/Intermediate/Advanced
    difficulty = db.Column(db.String(50), nullable=True)
    enrollment_count = db.Column(db.Integer, default=0)
    tags = db.Column(db.String(255), nullable=True)  # Comma-separated tags
    ratings = db.Column(db.Float, default=0)
    review_count = db.Column(db.Integer, default=0)
    objectives = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    # SerializerMixin allows .to_dict() and .to_json() methods
