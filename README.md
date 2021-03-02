# maddies-plant-shop
A web page that displays the plant stock from a plant shop from the database via a Python REST API.
 
# Getting Started
 
Clone this repository onto your machine. 
 
Pip and Python are required to run this application
 
To download Pip and Python:
https://pypi.org/project/pip/
https://www.python.org/downloads/
 
Install the dependencies by opening the command line and entering:
`Pip install -r requirements.txt`
 
Ensure that you are in the back_end folder in the command line.
Use cd and navigate to the folder if not.
 
Type the following commands into the command line:
 
`export FLASK_APP=rest_api.py`
`export FLASK_ENV=development`
`flask run`
 
Click the `Go Live` button on the bottom right of your VS Code to start your front end server.

Navigate to `http://localhost:5500/front_end/html/plants-homepage.html` in chrome browser


This will open the front-end UI.

# Tests
To test the Python REST API, navigate to `/back_end/python` and enter the command:
`python -m pytest -v`


# View database in browser
To view all the data in the plants_data table:

Navigate to `http://localhost:5000/browser_plants_data` in chrome browser while Flask app is running.

 
# Dependencies
aniso8601==8.1.0
atomicwrites==1.4.0
attrs==20.3.0
click==7.1.2
colorama==0.4.4
Flask==1.1.2
Flask-Jsonpify==1.5.0
Flask-RESTful==0.3.8
Flask-SQLAlchemy==2.4.4
iniconfig==1.1.1
itsdangerous==1.1.0
Jinja2==2.11.2
jsonify==0.5
MarkupSafe==1.1.1
packaging==20.7
pluggy==0.13.1
py==1.9.0
pyparsing==2.4.7
pytest==6.1.2
pytz==2020.4
six==1.15.0
SQLAlchemy==1.3.20
toml==0.10.2
Werkzeug==1.0.1
