from flask import Blueprint,render_template
from . import db
from sqlalchemy import text 

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("competitor.html")

@views.route('/test-db')
def test_db():
    try:
        db.session.execute(text('SELECT 1'))
        return "Database connection successful!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"