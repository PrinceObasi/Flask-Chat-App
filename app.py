# app.py
from os.path import join, dirname
from dotenv import load_dotenv
import os
import datetime
import flask
import flask_sqlalchemy
import flask_socketio
from rfc3987 import parse
import chatbot

################################

ADDRESSES_RECEIVED_CHANNEL = "addresses received"

app = flask.Flask(__name__)

socketio = flask_socketio.SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "sql.env")
load_dotenv(dotenv_path)

database_uri = os.getenv("DATABASE_URL")

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri

db = flask_sqlalchemy.SQLAlchemy(app)
db.init_app(app)
db.app = app

db.create_all()
db.session.commit()

import models

################################

# Temporary Server Data
numUsers = 0
userList = []

################################

# New Data Recieved - Username Logins and new Chats


@socketio.on("account - Request Username")
def on_username_request(data):
    print("Someone requested a new username: " + data["username"])

    nameTaken = False
    for user in db.session.query(models.Users).all():
        if user.username == data["username"]:
            nameTaken = True

    global numUsers
    numUsers += 1
    print("Number of Users Online: " + str(numUsers))

    if not nameTaken:
        db.session.add(models.Users(data["username"], data["imageUrl"]))
        db.session.commit()

    update_messages()
    update_user_count()

    socketio.emit(
        "account - Request Username Response",
        {
            "status": 1,
            "username": data["username"],
        },
    )


@socketio.on("chat - New Message")
def handle_new_message(data):
    db.session.add(
        models.Messages(
            data["username"],
            data["messageText"][0:256],
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            models.Users.query.filter_by(username=data["username"]).first().imageUrl,
        )
    )
    if data["messageText"][0:2] == "!!":
        db.session.add(
            models.Messages(
                "butler-bot",
                chatbot.respond(data["messageText"]),
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "https://i.imgur.com/m9mlpmh.png",
            )
        )
    db.session.commit()
    update_messages()
    return models.Messages(
        data["username"],
        data["messageText"][0:256],
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        models.Users.query.filter_by(username=data["username"]).first().imageUrl,
    )


# Updating User Counts and MessageHistory


def update_messages():
    print("Sending MessageHistory to All Clients")
    allMessages = []

    for message in db.session.query(models.Messages).order_by(models.Messages.id).all():
        try:
            print(
                "URL message detected: " + str(parse(message.messageText, rule="IRI"))
            )
            if (
                message.messageText[-4:] == ".gif"
                or message.messageText[-4:] == ".jpg"
                or message.messageText[-4:] == ".png"
            ):
                allMessages.append(
                    {
                        "username": message.username,
                        "messageText": message.messageText,
                        "timestamp": message.timestamp,
                        "imageUrl": message.imageUrl,
                        "messageType": 2,
                    }
                )
            else:
                allMessages.append(
                    {
                        "username": message.username,
                        "messageText": message.messageText,
                        "timestamp": message.timestamp,
                        "imageUrl": message.imageUrl,
                        "messageType": 3,
                    }
                )
        except:
            print("Message was not a URL")
            allMessages.append(
                {
                    "username": message.username,
                    "messageText": message.messageText,
                    "timestamp": message.timestamp,
                    "imageUrl": message.imageUrl,
                    "messageType": 1,
                }
            )

    socketio.emit(
        "chat - Update Messages",
        {
            "allMessages": allMessages,
        },
    )


def update_user_count():
    global numUsers
    socketio.emit("account - Update User Info", {"count": numUsers})


# Handling Disconnects


@socketio.on("disconnect")
def on_disconnect():
    global numUsers
    if numUsers > 0:
        numUsers -= 1
    update_user_count()
    print("Someone Disconnected. Remaining Users: " + str(numUsers))


################################


@app.route("/")
def index():
    # emit_all_addresses(ADDRESSES_RECEIVED_CHANNEL)
    return flask.render_template("index.html")


if __name__ == "__main__":
    socketio.run(
        app,
        host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", 8080)),
        debug=True,
    )
