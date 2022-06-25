from flask import Flask
from config import Configuration
from data import db_session

app = Flask(__name__)
app.config.from_object(Configuration)


def run():
    db_session.global_init()
    app.run()
