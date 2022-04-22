from flask import Flask, render_template, request
from models import db, connect_to_db
import models

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/add-user", methods=["POST"])
def add_user():
    username = request.form.get("username")
    email = request.form.get("email")
    res = models.add_user(username, email)
    return res["res"]

if __name__ == "__main__":
    connect_to_db(app)
    app.env = "development"
    app.run(port=80, host="localhost", debug=True)