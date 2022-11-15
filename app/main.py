from flask import Flask, render_template, request
from Fortuna import dice

APP = Flask(__name__)


@APP.route("/", methods=["GET", "POST"])
def home_page():
    rolls = request.values.get("rolls", "1")
    sides = request.values.get("sides", "10")
    rand_number = dice(int(rolls), int(sides))
    return render_template("home.html", number=rand_number)


@APP.route("/about")
def about_page():
    return render_template("about.html")


@APP.route("/contact")
def contact_page():
    return render_template("contact.html")
