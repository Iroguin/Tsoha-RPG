from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from dotenv import load_dotenv

load_dotenv("/Users/eddie/Tsoha-RPG/closet/.env")

app = Flask(__name__, template_folder="templates")
app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)

if '__main__' == __name__:
    app.run()

import routes