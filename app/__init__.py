# Package identifier

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# when you do app factory you will work in application context
db = SQLAlchemy()

def create_app():
    """ Make the app"""
    # object relational configuration need instance rel config. 
    # The configuration coming from outisde the object
    app = Flask(__name__, instance_relative_config=False)

    # Have the app know about the database
    app.config.from_object("config.Config")
    
    # inform the sqlalchemy DB about the app
    db.init_app(app)

    # open app_context method
    with app.app_context():

        # import our routes
        from . import routes

        # create the database and tables
        db.create_all()

        return app

