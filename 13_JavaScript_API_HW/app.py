import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template

engine = create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Samples = Base.classes.samples
Samples_Metadata = Base.classes.samples_metadata
OTU = Base.classes.otu

session = Session(engine)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/names')
def names():
    stmnt = session.query(Samples).statement
    df = pd.read_sql_query(stmnt, session.bind)
    df.set_index('otu_id', inplace=True)
    return jsonify(list(df.columns))


@app.route('/otu')
def otu():
    results = session.query(OTU.lowest_taxonomic_unit_found).all()
    otu_list = list(np.ravel(results))
    return jsonify(otu_list)


@app.route('/metadata/<sample>')
def sample_metadata(sample):
    sel = [Samples_Metadata.SAMPLEID, Samples_Metadata.ETHNICITY,
           Samples_Metadata.GENDER, Samples_Metadata.AGE,
           Samples_Metadata.LOCATION, Samples_Metadata.BBTYPE]
    results = session.query(*sel).\
        filter(Samples_Metadata.SAMPLEID == sample[3:]).all()
    sample_metadata = {}
    for result in results:
        sample_metadata['SAMPLEID'] = result[0]
        sample_metadata['ETHNICITY'] = result[1]
        sample_metadata['GENDER'] = result[2]
        sample_metadata['AGE'] = result[3]
        sample_metadata['LOCATION'] = result[4]
        sample_metadata['BBTYPE'] = result[5]
    return jsonify(sample_metadata)


@app.route('/wfreq/<sample>')
def sample_wfreq(sample):
    results = session.query(Samples_Metadata.WFREQ).\
        filter(Samples_Metadata.SAMPLEID == sample[3:]).all()
    wfreq = np.ravel(results)
    return jsonify(int(wfreq[0]))


@app.route('/samples/<sample>')
def samples(sample):
    stmnt = session.query(Samples).statement
    df = pd.read_sql_query(stmnt, session.bind)
    if sample not in df.columns:
        return jsonify(f"Error! Sample: {sample} Not Found!")
    df = df[df[sample] > 1]
    df = df.sort_values(by=sample, ascending=0)
    data = [{
        "otu_ids": df[sample].index.values.tolist(),
        "sample_values": df[sample].values.tolist()
    }]
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
