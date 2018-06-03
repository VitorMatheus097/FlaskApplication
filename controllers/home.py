import datetime
from flask import render_template
from flask import Flask, request, render_template

from app import app
from app.models.database import DataBase

currentYear = datetime.datetime.now()

@app.route("/", methods=["GET"])
def index():
    return render_template('home.html', currentYear = currentYear.year)

@app.route("/", methods=["POST"])
def process_data():
    text = request.form.get("text")
    db = DataBase()

    return render_template('show-text.html', text = text, db=db, currentYear = currentYear.year)


@app.route("/about", methods=["GET"])
def about():
    return render_template('about.html', currentYear = currentYear.year)


