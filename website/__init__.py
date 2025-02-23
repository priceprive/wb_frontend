from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


db = SQLAlchemy() 
DB_NAME = "database.db"

def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='pp'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:priceprive%402024@localhost:5432/priceprive'

    #app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:Ritika%402001@localhost:5432/priceprive'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User
    # ,Note 

    with app.app_context():
        try:
            print("Attempting to create tables...")
            db.create_all()
            db.session.commit()
            print("Tables created successfully")
        except Exception as e:
            print(f"Error creating tables: {str(e)}")



        #     db.create_all()
        #     print("Tables created successfully")
        # except Exception as e:
        #     print(f"Error creating tables: {str(e)}")
        # db.create_all()

    return app

    # create_database(app)

    # return app

# def create_database(app):
#     if not path.exists('website/' + DB_NAME):
#         db.create_all(app=app)
#         print('Created Database!')