import os

import json

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/licenses.sqlite"
db = SQLAlchemy(app)
engine = create_engine("sqlite:///db/licenses.sqlite")


class License(db.Model):
    __tablename__ = 'licenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    classification = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)

    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return '<License %r>' % (self.name)


@app.before_first_request
def setup():
    db.create_all()

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("dashboard.html")

@app.route("/map")
def cluster_map():
    """Return the homepage."""
    return render_template("index.html")


# loads geojson into server so it can be called by our js
@app.route("/neighborhoods")
def neighborhoods():
    path = 'static/Resources/statistical_neighborhoods.geojson'
    with open(path) as f:
        data = json.load(f)
    for feature in data['features']:
        print(feature['properties'])
    return jsonify(data)

@app.route("/licenses")
def licensetype():
    path = 'static/Resources/license_data.geojson'
    with open(path) as f:
        data = json.load(f)
    for feature in data['features']:
        print(feature['properties'])
    return jsonify(data)

@app.route("/chartdata")
def license():

    license_test = engine.execute(
        "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

    
    rows = list(license_test.fetchall())
    counts = []
    liquor_type = []
    for row_result in rows:
        counts.append(row_result["countBiz"])
        liquor_type.append(row_result["field3"])

    # return "hey"  # jsonify(trace)
    return jsonify({
        "x":liquor_type,
        "y":counts, 
        "type": "bar"
        
    })


@app.route("/chart")
def chart():
    """Return the homepage."""
    return render_template("chart.html")


@app.route("/piedata")
def license_pie():

    license_test = engine.execute(
        "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

    rows = list(license_test.fetchall())
    counts = []
    liquor_type = []
    for row_result in rows:
        counts.append(row_result["countBiz"])
        liquor_type.append(row_result["field3"])

    return jsonify({
        "labels":liquor_type,
        "values":counts, 
        "type": "pie"
        
    })


@app.route("/pie")
def pie():
    """Return the homepage."""
    return render_template("pie.html")


if __name__ == "__main__":
    app.run()
