from flask import Flask, render_template, request


APP = Flask(__name__)


@APP.route("/")
def home_page():
    return render_template("home.html")


@APP.route("/about")
def about_page():
    return render_template("about.html")


@APP.route("/contact")
def contact_page():
    return render_template("contact.html")
