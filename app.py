#=======================
#   Dependencies
#=======================
import numpy as np
import pandas as pd
import logging
import sqlalchemy
import datetime as dt
import sys
sys.path.append("static/assets/resources/")
import config as c
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.pool import StaticPool
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy



#======================
#   Initialize Flask App
#======================
app = Flask(__name__)

#=====================
#DB connection
#=====================
conn_string = f"{c.username}:{c.password}@localhost/bbb_db"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{conn_string}"

db = SQLAlchemy(app)

engine = create_engine(f'mysql://{conn_string}')

#=====================
#Define models
#=====================

#Sample Model
class Sample(db.Model):
    __tablename__= "samples"
    id = db.Column(db.Integer, primary_key=True)
    otu_id = db.Column(db.Integer)
    otu_label = db.Column(db.String(100))
    BB_940 = db.Column(db.Integer)
    BB_941 = db.Column(db.Integer)
    BB_943 = db.Column(db.Integer)
    BB_944 = db.Column(db.Integer)
    BB_945 = db.Column(db.Integer)
    BB_946 = db.Column(db.Integer)
    BB_947 = db.Column(db.Integer)
    BB_948 = db.Column(db.Integer)
    BB_949 = db.Column(db.Integer)
    BB_950 = db.Column(db.Integer)
    BB_952 = db.Column(db.Integer)
    BB_953 = db.Column(db.Integer)
    BB_954 = db.Column(db.Integer)
    BB_955 = db.Column(db.Integer)
    BB_956 = db.Column(db.Integer)
    BB_958 = db.Column(db.Integer)
    BB_959 = db.Column(db.Integer)
    BB_960 = db.Column(db.Integer)
    BB_961 = db.Column(db.Integer)
    BB_962 = db.Column(db.Integer)
    BB_963 = db.Column(db.Integer)
    BB_964 = db.Column(db.Integer)
    BB_966 = db.Column(db.Integer)
    BB_967 = db.Column(db.Integer)
    BB_968 = db.Column(db.Integer)
    BB_969 = db.Column(db.Integer)
    BB_970 = db.Column(db.Integer)
    BB_971 = db.Column(db.Integer)
    BB_972 = db.Column(db.Integer)
    BB_973 = db.Column(db.Integer)
    BB_974 = db.Column(db.Integer)
    BB_975 = db.Column(db.Integer)
    BB_978 = db.Column(db.Integer)
    BB_1233 = db.Column(db.Integer)
    BB_1234 = db.Column(db.Integer)
    BB_1235 = db.Column(db.Integer)
    BB_1236 = db.Column(db.Integer)
    BB_1237 = db.Column(db.Integer)
    BB_1238 = db.Column(db.Integer)
    BB_1242 = db.Column(db.Integer)
    BB_1243 = db.Column(db.Integer)
    BB_1246 = db.Column(db.Integer)
    BB_1253 = db.Column(db.Integer)
    BB_1254 = db.Column(db.Integer)
    BB_1258 = db.Column(db.Integer)
    BB_1259 = db.Column(db.Integer)
    BB_1260 = db.Column(db.Integer)
    BB_1264 = db.Column(db.Integer)
    BB_1265 = db.Column(db.Integer)
    BB_1273 = db.Column(db.Integer)
    BB_1275 = db.Column(db.Integer)
    BB_1276 = db.Column(db.Integer)
    BB_1277 = db.Column(db.Integer)
    BB_1278 = db.Column(db.Integer)
    BB_1279 = db.Column(db.Integer)
    BB_1280 = db.Column(db.Integer)
    BB_1281 = db.Column(db.Integer)
    BB_1282 = db.Column(db.Integer)
    BB_1283 = db.Column(db.Integer)
    BB_1284 = db.Column(db.Integer)
    BB_1285 = db.Column(db.Integer)
    BB_1286 = db.Column(db.Integer)
    BB_1287 = db.Column(db.Integer)
    BB_1288 = db.Column(db.Integer)
    BB_1289 = db.Column(db.Integer)
    BB_1290 = db.Column(db.Integer)
    BB_1291 = db.Column(db.Integer)
    BB_1292 = db.Column(db.Integer)
    BB_1293 = db.Column(db.Integer)
    BB_1294 = db.Column(db.Integer)
    BB_1295 = db.Column(db.Integer)
    BB_1296 = db.Column(db.Integer)
    BB_1297 = db.Column(db.Integer)
    BB_1298 = db.Column(db.Integer)
    BB_1308 = db.Column(db.Integer)
    BB_1309 = db.Column(db.Integer)
    BB_1310 = db.Column(db.Integer)
    BB_1374 = db.Column(db.Integer)
    BB_1415 = db.Column(db.Integer)
    BB_1439 = db.Column(db.Integer)
    BB_1441 = db.Column(db.Integer)
    BB_1443 = db.Column(db.Integer)
    BB_1486 = db.Column(db.Integer)
    BB_1487 = db.Column(db.Integer)
    BB_1489 = db.Column(db.Integer)
    BB_1490 = db.Column(db.Integer)
    BB_1491 = db.Column(db.Integer)
    BB_1494 = db.Column(db.Integer)
    BB_1495 = db.Column(db.Integer)
    BB_1497 = db.Column(db.Integer)
    BB_1499 = db.Column(db.Integer)
    BB_1500 = db.Column(db.Integer)
    BB_1501 = db.Column(db.Integer)
    BB_1502 = db.Column(db.Integer)
    BB_1503 = db.Column(db.Integer)
    BB_1504 = db.Column(db.Integer)
    BB_1505 = db.Column(db.Integer)
    BB_1506 = db.Column(db.Integer)
    BB_1507 = db.Column(db.Integer)
    BB_1508 = db.Column(db.Integer)
    BB_1510 = db.Column(db.Integer)
    BB_1511 = db.Column(db.Integer)
    BB_1512 = db.Column(db.Integer)
    BB_1513 = db.Column(db.Integer)
    BB_1514 = db.Column(db.Integer)
    BB_1515 = db.Column(db.Integer)
    BB_1516 = db.Column(db.Integer)
    BB_1517 = db.Column(db.Integer)
    BB_1518 = db.Column(db.Integer)
    BB_1519 = db.Column(db.Integer)
    BB_1521 = db.Column(db.Integer)
    BB_1524 = db.Column(db.Integer)
    BB_1526 = db.Column(db.Integer)
    BB_1527 = db.Column(db.Integer)
    BB_1530 = db.Column(db.Integer)
    BB_1531 = db.Column(db.Integer)
    BB_1532 = db.Column(db.Integer)
    BB_1533 = db.Column(db.Integer)
    BB_1534 = db.Column(db.Integer)
    BB_1535 = db.Column(db.Integer)
    BB_1536 = db.Column(db.Integer)
    BB_1537 = db.Column(db.Integer)
    BB_1539 = db.Column(db.Integer)
    BB_1540 = db.Column(db.Integer)
    BB_1541 = db.Column(db.Integer)
    BB_1542 = db.Column(db.Integer)
    BB_1543 = db.Column(db.Integer)
    BB_1544 = db.Column(db.Integer)
    BB_1545 = db.Column(db.Integer)
    BB_1546 = db.Column(db.Integer)
    BB_1547 = db.Column(db.Integer)
    BB_1548 = db.Column(db.Integer)
    BB_1549 = db.Column(db.Integer)
    BB_1550 = db.Column(db.Integer)
    BB_1551 = db.Column(db.Integer)
    BB_1552 = db.Column(db.Integer)
    BB_1553 = db.Column(db.Integer)
    BB_1554 = db.Column(db.Integer)
    BB_1555 = db.Column(db.Integer)
    BB_1556 = db.Column(db.Integer)
    BB_1557 = db.Column(db.Integer)
    BB_1558 = db.Column(db.Integer)
    BB_1561 = db.Column(db.Integer)
    BB_1562 = db.Column(db.Integer)
    BB_1563 = db.Column(db.Integer)
    BB_1564 = db.Column(db.Integer)
    BB_1572 = db.Column(db.Integer)
    BB_1573 = db.Column(db.Integer)
    BB_1574 = db.Column(db.Integer)
    BB_1576 = db.Column(db.Integer)
    BB_1577 = db.Column(db.Integer)
    BB_1581 = db.Column(db.Integer)
    BB_1601 = db.Column(db.Integer)
    sample_values = db.Column(db.Integer)

    def __repr__(self):
        return '<Samples %r>' % (self.name)

#Metadata Model
class MetaD(db.Model):
    __tablename__ = "metad"

    id = db.Column(db.Integer, primary_key=True)
    sample = db.Column(db.Integer)
    _EVENT = db.Column(db.String(100))
    ETHNICITY = db.Column(db.String(100))
    GENDER = db.Column(db.String(100))
    AGE = db.Column(db.Integer)
    WFREQ = db.Column(db.Float)
    BBTYPE = db.Column(db.String(100))
    LOCATION = db.Column(db.String(100))
    COUNTRY012 = db.Column(db.String(100))
    ZIP012 = db.Column(db.Integer)
    COUNTRY1319 = db.Column(db.String(100))
    ZIP1319= db.Column(db.Integer)
    DOG = db.Column(db.String(100))
    CAT = db.Column(db.String(100))
    IMPSURFACE013 = db.Column(db.Integer)
    NPP013 = db.Column(db.Float)
    MMAXTEMP013 = db.Column(db.Float)
    PFC013 = db.Column(db.Integer)
    IMPSURFACE1319 = db.Column(db.Integer)
    NPP1319 = db.Column(db.Integer)
    MMAXTEMP1319 = db.Column(db.Float)
    PFC1319 = db.Column(db.Float)

    def __repr__(self):
        return '<MetaD %r>' % (self.name)

#===============================
#   Helper functions
#===============================


#Global Variables
top_otu_id = []
top_otu_labels = []
top_sample_values = []
sample = "BB_940"


#Get Top 10 values for plots
def top10(sample):
    sample = sample
    top_otu_id = []
    top_otu_labels = []
    top_sample_values = []

    #Clean sample number input. Remove "BB_" 
    s = str(sample[3:])
    with engine.connect() as con:
        results = con.execute("SELECT otu_id, otu_label, `" + s + "` FROM samples ORDER BY `"+ s + "` DESC LIMIT 10")
        
        # results = db.session.query(Sanmple.otu_id, Sample.otu_label, Sample.s)

    for r in results:
    
        top_otu_id.append(r["otu_id"])
        top_otu_labels.append(r["otu_label"])
        top_sample_values.append(r[s])
        #top_otu_id, top_otu_labels, top_sample_values
    samp_data = [
        top_otu_id,
        top_otu_labels,
        top_sample_values
    ]
    return samp_data
     
#Get sample metadata for display
def getMeta(sample):
    sample = sample
    #Clean sample number input. Remove "BB_"
    s = sample[3:]
    with engine.connect() as con:
        metaData = con.execute("SELECT AGE, BBTYPE, ETHNICITY, LOCATION, sample FROM metad WHERE sample =" + s)
    return metaData




#Seed DB 
def loadSamples():
    csv = "static/assets/resources/data/belly_button_data.csv"
    Sample_df = pd.read_csv(csv, encoding='utf-8')
    Sample_df["sample_values"] = (Sample_df.sum(axis=1) - Sample_df["otu_id"])
    Sample_df.to_sql(name='samples', con=engine, if_exists = 'replace', index=True)


def loadMetaD():
    csv = "static/assets/resources/data/belly_button_metadata.csv"
    MetaD_df = pd.read_csv(csv, encoding='utf-8')
    MetaD_df.to_sql(name='metad', con=engine, if_exists = 'replace', index=True)

#======================
#Page load functions
#======================
# Build database and tables from models
@app.before_first_request
def build():
    #Drop existing DB
    db.drop_all()
    #Rebuild DB and tables from models
    db.create_all()
    #Load the tables with data from csv files
    loadSamples()
    loadMetaD()
    top10("BB_940")

#================================
#   Routes
#================================

#Root
@app.route("/")
def dashboard():
    return render_template("index.html")

#Get Top ten sample data
@app.route("/sample/<sample>")
def sample(sample):
    #Call top10(sample) to get sample data for plots
    samp_data = top10(sample)
    #Call getMeta(sample) to get sample metadata
    metaData = getMeta(sample)

    sample_data = [{
        "pie_data": [{
            "name": "Top 10 Belly Button Bacteria Samples",
            "values": samp_data[2],
            "labels": samp_data[0],
            "hoverinfo": samp_data[1],
            "type": "pie"
        }],
        "bubble_data": [{
            "x": samp_data[0],
            "y": samp_data[2],
           " mode": "markers",
            "marker": {
                "size": samp_data[2],
               " color": samp_data[0]
            },
            "text": samp_data[1]
        }],
        "metadata": [dict(row) for row in metaData]
    }]

    return jsonify(sample_data)

if __name__ == '__main__':
    app.run(debug=True)