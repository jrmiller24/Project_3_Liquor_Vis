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

# import Granim from 'react-granim'
 
app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/licenses.sqlite"
db = SQLAlchemy(app)
engine = create_engine("sqlite:///db/licenses.sqlite")

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each table
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples


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
    # Recreate database each time for demo
    # db.drop_all()
    db.create_all()


# @app.route("/send", methods=["GET", "POST"])
# def send():
#     if request.method == "POST":
#         name = request.form["field1"]
#         address = request.form["field2"]
#         classification = request.form["field3"]
#         city = request.form["field4"]
#         state = request.form["field5"]

#         latitude = request.form["field6"]
#         longitude = request.form["field7"]


#         license = License(name=name, address=address, classification=classification, city=city, state=state, latitude=latitude, longitude=longitude)
#         db.session.add(license)
#         db.session.commit()
#         return redirect("/", code=302)

#     return render_template("chart.html")


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


@app.route("/chartdata")
def license():

    license_test = engine.execute(
        "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

    # license_count = db.session.query(db.field3)#, func.count(db.field3)).group_by(db.field3).all()

    # license_type = [licenses.field3]
    # license_count = [result[1] for result in results]

    # trace = {
    #     "x": license_type,
    #     "y": license_count,
    #     "type": "bar"
    # }

    #db.session.query (func.count(licenses.field3))
    # return jsonify([{
    #     "field3": row['field3'],
    #     "count": row["countBiz"]
    # } for row in license_test.fetchall()])  
    rows = list(license_test.fetchall())
    #print(rows[0])
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

# @app.route('/chart')
# def pie():

#     license_test = engine.execute(
#         "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

#     rows = list(license_test.fetchall())
#     #print(rows[0])
#     counts = []
#     liquor_type = []
#     for row_result in rows:
#         counts.append(row_result["countBiz"])
#         liquor_type.append(row_result["field3"])

#     return jsonify({
#         labels:liquor_type,
#         values:counts,
#         "type": "pie"


@app.route("/chart")
def chart():
    """Return the homepage."""
    return render_template("chart.html")


@app.route("/piedata")
def license_pie():

    license_test = engine.execute(
        "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

    # license_count = db.session.query(db.field3)#, func.count(db.field3)).group_by(db.field3).all()

    # license_type = [licenses.field3]
    # license_count = [result[1] for result in results]

    # trace = {
    #     "x": license_type,
    #     "y": license_count,
    #     "type": "bar"
    # }

    #db.session.query (func.count(licenses.field3))
    # return jsonify([{
    #     "field3": row['field3'],
    #     "count": row["countBiz"]
    # } for row in license_test.fetchall()])  
    rows = list(license_test.fetchall())
    #print(rows[0])
    counts = []
    liquor_type = []
    for row_result in rows:
        counts.append(row_result["countBiz"])
        liquor_type.append(row_result["field3"])

    # return "hey"  # jsonify(trace)
    return jsonify({
        "labels":liquor_type,
        "values":counts, 
        "type": "pie"
        
    })

# @app.route('/chart')
# def pie():

#     license_test = engine.execute(
#         "SELECT field3, COUNT(field3) AS countBiz FROM licenses  GROUP BY field3")

#     rows = list(license_test.fetchall())
#     #print(rows[0])
#     counts = []
#     liquor_type = []
#     for row_result in rows:
#         counts.append(row_result["countBiz"])
#         liquor_type.append(row_result["field3"])

#     return jsonify({
#         labels:liquor_type,
#         values:counts,
#         "type": "pie"


@app.route("/pie")
def pie():
    """Return the homepage."""
    return render_template("pie.html")


if __name__ == "__main__":
    app.run()
