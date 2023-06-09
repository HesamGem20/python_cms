"""
This module defines the database models for the blog posts.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Post(db.Model):
    """
    Represents a blog post.
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
