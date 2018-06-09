import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
warnings.filterwarnings('ignore')

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Hawaii.sqlite")

# reflect the database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Station = Base.classes.station
Measurements = Base.classes.measurements

# Create our session (link) from Python to the DB
session = Session(engine)

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"

        f"/api/v1.0/precipitation - List of rain totals from all stations from previous year<br/>"

        f"/api/v1.0/stations - List of Station numbers and names<br/>"

        f"/api/v1.0/tobs - List of temperatures from all stations from previous year<br/>"

        f"/api/v1.0/start - Given the start date (YYYY-MM-DD), calculates the MIN/AVG/MAX temperature for all dates greater than and equal to the start date<br/>"

        f"/api/v1.0/start/end - Given the start and the end date (YYYY-MM-DD), calculate the MIN/AVG/MAX temperature for dates between the start and end date<br/>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_year = dt.date(2018, 3, 6) - dt.timedelta(days=365)
    results = session.query(Measurements.date, Measurements.prcp).filter(Measurements.date > last_year).order_by(Measurements.date).all()

    rain_totals = []
    for result in results:
        row = {}
        row["date"] = rain[0]
        row["prcp"] = rain[1]
        rain_totals.append(row)

    return jsonify(rain_totals)


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.name, Station.station)
    all_stations = list(np.ravel(results))
    return jsonify(all_stations)


@app.route("/api/v1.0/tobs")
def tobs():
    last_date = session.query(Measurements.date).order_by(Measurements.date.desc()).first()
    last_year = dt.date(2018, 3, 6) - dt.timedelta(days=365)
    results = session.query(Measurements.date, Measurements.tobs).filter(Measurements.date > last_year).order_by(Measurements.date).all()

    temp_totals = []
    for result in results:
        row = {}
        row["date"] = temperature[0]
        row["tobs"] = temperature[1]
        temp_totals.append(row)

    return jsonify(temp_totals)


@app.route("/api/v1.0/<start>")
def temps(start):
    start= dt.datetime.strptime(start, '%Y-%m-%d')
    temp_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).filter(Measurements.date >= start).all()
    temps = list(np.ravel(temp_data))
    return jsonify(temps)


@app.route("/api/v1.0/<start>/<end>")
def temprange(start,end):
    start= dt.datetime.strptime(start, '%Y-%m-%d')
    end= dt.datetime.strptime(end,'%Y-%m-%d')
    trip_data = session.query(func.min(Measurements.tobs), func.avg(Measurements.tobs), func.max(Measurements.tobs)).\
        filter(Measurements.date >= start).filter(Measurements.date <= end).all()
    temprange = list(np.ravel(trip_data))
    return jsonify(temprange)


if __name__ == '__main__':
    app.run(debug=True)