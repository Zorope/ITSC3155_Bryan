# FLASK Tutorial 1 -- We show the bare bones code to get an app up and running

# imports
import os                 # os is used to get environment variables IP & PORT
from flask import Flask   # Flask is the web app that we will customize
from flask import render_template
from flask import request

app = Flask(__name__)     # create an app

# @app.route is a decorator. It gives the function "index" special powers.
# In this case it makes it so anyone going to "your-url/" makes this function
# get called. What it returns is what is shown as the web page
@app.route('/index')
def index():
    a_user = {'name': 'Bryan', 'email': 'bryan@uncc.edu'}
    return render_template('index.html', user = a_user)

@app.route('/notes')
def get_notes():
    notes = {1:{'title': 'first note', 'text': 'this is my first note', 'date': '10-1-2020'},
            2:{'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
            3:{'title': 'Third note', 'text': 'this is my third note', 'date': '10-3-2020'}}
    a_user = {'name': 'Bryan', 'email': 'mogli@uncc.edu'}
    return render_template('notes.html', notes=notes, user=a_user)

@app.route('/notes/<note_id>')
def get_note(note_id):
    notes = {1:{'title': 'first note', 'text': 'this is my first note', 'date': '10-1-2020'},
            2:{'title': 'Second note', 'text': 'this is my second note', 'date': '10-2-2020'},
            3:{'title': 'Third note', 'text': 'this is my third note', 'date': '10-3-2020'}}
    a_user = {'name': 'Bryan', 'email': 'mogli@uncc.edu'}
    return render_template('note.html', note=notes[int(note_id)], user=a_user)

@app.route('/notes/new', methods=['GET','POST'])
def new_note():
    print('request method is', request.method)
    a_user = {'name': 'Mogli', 'email': 'mogli@uncc.edu'}
    if request.method == 'POST':
        request_data = request.form
        return f"data: {request_data} !"
    else:
        return render_template('new.html', user=a_user)

app.run(host=os.getenv('IP', '127.0.0.1'),port=int(os.getenv('PORT', 5000)),debug=True)

# To see the web page in your web browser, go to the url,
#   http://127.0.0.1:5000

# Note that we are running with "debug=True", so if you make changes and save it
# the server will automatically update. This is great for development but is a
# security risk for production.