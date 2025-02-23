from flask import Blueprint 
from . import db
from sqlalchemy import text 

views = Blueprint('views',__name__)

# @views.route('/')
# def home():
#     return "<h1>Test</h1>"

@views.route('/test-db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"