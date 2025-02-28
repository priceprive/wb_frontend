from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()


class Note(db.Model) :
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column (db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column (db.Integer, db.ForeignKey ('user.id'))


#     def __repr__(self):
#         return f'<Note {self.id}>'

class User(db.Model,UserMixin):
    __tablename__ = 'user'
    # __table_args__ = {'schema': 'public'} 
     # Explicitly define the schema as 'public'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), nullable=False)
    # phone = db.Column(db.String(15), nullable=False)
    notes = db.relationship('Note')

    def __repr__(self):
        return f'<User {self.email}>'



