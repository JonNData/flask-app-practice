# the routes of the app, this is the roadmap and all the action for the urls

from flask import  render_template, url_for, redirect, make_response, request
from flask import current_app as app
from .models import *
from urllib import request as rq
import json


# url_for will construct a hypertext link, similar to a_href

@app.route('/', methods=['GET', 'POST']) 
# Get is inferred method to interact with http. Endpoint point of access
def home():
    """ When browser pings this enpoint, display the home page"""
    return render_template("home.html")

@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():

    if request.method == 'POST':
        name = request.form['username']
        city = request.form['city']
        occupation = request.form['occupation']

        new_user = User(name=name, city=city, occupation=occupation)
        user_exists = User.query.filter_by(name=name).first()
        if user_exists:
            return make_response(f"User {name} already exists")

        db.session.add(new_user)
        db.session.commit()
        return make_response(f"User {name} Successfully Created!")


@app.route('/savedata', methods = ['GET', 'POST'])
def savedata():
    # the api data we get back is serialized dictionary of dictionaries
    """ Calls openaq and saves DB"""
    url = rq.urlopen('https://api.openaq.org/v1/cities/?country=AU')
    data = url.read()

    # parse the data
    new_data = json.loads(data.decode('utf-8'))
    new_data = new_data['results']

    # Loops over list of dicts to extract values
    for i in range(len(new_data)):
        row = list()
        for value in new_data[i].values():
            row.append(value)
        
        # now construct the class
        row_data = OpenAQ(
            country=row[0], name=row[1], city=row[2], 
            count=row[3], locations=row[4])
        
        # prepare for addition to Database
        db.session.add(row_data)
    db.session.commit()
    return "Success!"