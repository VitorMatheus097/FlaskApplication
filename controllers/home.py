from flask import render_template
from flask import Flask, request, render_template

from app import app
from app.models.database import DataBase

@app.route("/", methods=["GET"])
def index():
    return render_template('home.html')

@app.route("/", methods=["POST"])
def process_data():
    text = request.form.get("text")
    db = DataBase()
    
    return render_template('show-text.html', text = text)