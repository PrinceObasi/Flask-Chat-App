


# What is Project2?
Hi! This project is a simple webapp designed to be a simpel chatroom using a variety of API and frameworks. This project was created for CS490 section 003 at NJIT.

# Project Description
![enter image description here](https://i.imgur.com/YXmfLkn.jpg)

This project is designed to practice using multiple technologies together in a single project, such as socketio, postgresql, SQLALchemy, flask, react, etc. The point is to combine frontend and backend elements to create a "complex" project to develop experience making more real-to-life webapps. Neat stuff huh?

# Setup
As a general overview, here are the python packages you'll need. Be sure to install them if you don't have them already:
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
	- `pip install Flask`
- [Socketio](https://flask-socketio.readthedocs.io/en/latest/)
	- `pip install flask-socketio`
- [axju-jokes](https://pypi.org/project/axju-jokes/)
	- `pip install axju-jokes`
- [python-dotenv](https://pypi.org/project/python-dotenv/)
	- `pip install python-dotenv`
- [requests](https://requests.readthedocs.io/en/master/)
	- `python -m pip install requests`
- [rfc3987](https://pypi.org/project/rfc3987/)
	- `python install rfc3987`

## Setting up React
Run the following commands to install the things you'll need for React.
1) `npm install`  
2) `pip install flask-socketio`  
3) `pip install eventlet`  
4) `npm install -g webpack`  
5) `npm install --save-dev webpack`  
6) `npm install socket.io-client --save`  

## Setting up PSQL
1)  `sudo yum update`, and enter yes to all prompts
2) Get psycopg2:  `sudo /usr/local/bin/pip install psycopg2-binary`
3)  Get SQLAlchemy:  `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`
4) `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
5) `sudo service postgresql initdb`
6) `sudo service postgresql start`
7) `sudo -u postgres createuser --superuser $USER`
8) `sudo -u postgres createdb $USER`
9) Enter `psql` to access the psql CLI
	1)  `create user [some_username_here] superuser password '[some_unique_new_password_here]';` replacing the [values] with a custom username and password. Remember these! You'll need them later!
	2) `\q` to exit psql
10)  make a new file in your project folder named `sql.env` and add the line `DATABASE_URL='postgresql://{username}:{password}@localhost/postgres'`. Be sure to replace `{username}` and `{password}` to the credentials you made in step 9

## Getting Started
To start, clone this repository by using
`git clone https://github.com/NJIT-CS490/project2_m2_rab63`

Make sure you set up your `sql.env` properly in Step 10 in the previous section. After that, run `npm run watch`, and in a new terminal naviagte back to your porject folder and run `python app.py` View the application and you should see the login screen for the chat app!

## Resolved Technical Issues
> Avatar Display Issue

One issue I ran into was that when I was trying to display a user's avatar in a message, all of the messages would collapse into a hellish cascade of messages with improper identation. After googling online about this issue, I realized I had to use a series of `float: left` and `display: inline-block` statements in my CSS, and that resolved the issue.

> Google User Data

At first, I wasn't able to access my user data because I wasn't sure what was contained in the response or its format. A simple `console.log(response)` showed me it was a json with the user's data, which also showed me the data fields. This allows me to pull the data and pass it to my server to create a user.

## Possible Improvements
1) One way I would improve this project if I had more time would be to allow users to edit their username. This would require keeping seperate database entires for userID (email) and username (their displayname).

2) A second way I would improve this project if I had more time would be to display an actual list of users that are currently online. This would require a temporary object to be created and updated as users join/leave the chat, and sent to each client periodically.