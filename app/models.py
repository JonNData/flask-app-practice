# These classes will be the tables in our DB
from app import db


class User(db.Model):
    """
    User class inherits from db, the Model which tells it that it is a db table
    """
    # name of column =  database column(datatype, extra params)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(255))
    occupation = db.Column(db.String(255))


class OpenAQ(db.Model):

    # if __tablename__ isn't specified, it will default to lower case "openaq"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    city = db.Column(db.String(255))
    country = db.Column(db.String(2))
    count = db.Column(db.Integer)
    locations = db.Column(db.Integer)
