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

#Seed DB Helper functions
def loadSamples():
    csv = "static/assets/resources/data/belly_button_data.csv"
    Sample_df = pd.read_csv(csv, encoding='utf-8')
    Sample_df.to_sql(name='samples', con=engine, if_exists = 'replace', index=True)
    # for s in Sample_df:
    #     sample = Sample(
    #         otu_id = s.otu_id,
    #         otu_label = s.otu_label,
    #         BB_940 = s.940,
    #         BB_941 = s.941,
    #         BB_943 = s.943,
    #         BB_944 = s.944,
    #         BB_945 = s.945,
    #         BB_946 = s.946,
    #         BB_947 = s.947,
    #         BB_948 = s.948,
    #         BB_949 = s.949,
    #         BB_950 = s.950,
    #         BB_952 = s.952,
    #         BB_953 = s.953,
    #         BB_954 = s.954,
    #         BB_955 = s.955,
    #         BB_956 = s.956,
    #         BB_958 = s.958,
    #         BB_959 = s.959,
    #         BB_960 = s.960,
    #         BB_961 = s.961,
    #         BB_962 = s.962,
    #         BB_963 = s.963,
    #         BB_964 = s.964,
    #         BB_966 = s.966,
    #         BB_967 = s.967,
    #         BB_968 = s.968,
    #         BB_969 = s.969,
    #         BB_970 = s.970,
    #         BB_971 = s.971,
    #         BB_972 = s.972,
    #         BB_973 = s.973,
    #         BB_974 = s.974,
    #         BB_975 = s.975,
    #         BB_978 = s.978,
    #         BB_1233 = s.1233,
    #         BB_1234 = s.1234,
    #         BB_1235 = s.1235,
    #         BB_1236 = s.1236,
    #         BB_1237 = s.1237,
    #         BB_1238 = s.1238,
    #         BB_1242 = s.1242,
    #         BB_1243 = s.1243,
    #         BB_1246 = s.1246,
    #         BB_1253 = s.1253,
    #         BB_1254 = s.1254,
    #         BB_1258 = s.1258,
    #         BB_1259 = s.1259,
    #         BB_1260 = s.1260,
    #         BB_1264 = s.1264,
    #         BB_1265 = s.1265,
    #         BB_1273 = s.1273,
    #         BB_1275 = s.1275,
    #         BB_1276 = s.1276,
    #         BB_1277 = s.1277,
    #         BB_1278 = s.1278,
    #         BB_1279 = s.1279,
    #         BB_1280 = s.1280,
    #         BB_1281 = s.1281,
    #         BB_1282 = s.1282,
    #         BB_1283 = s.1283,
    #         BB_1284 = s.1284,
    #         BB_1285 = s.1285,
    #         BB_1286 = s.1286,
    #         BB_1287 = s.1287,
    #         BB_1288 = s.1288,
    #         BB_1289 = s.1289,
    #         BB_1290 = s.1290,
    #         BB_1291 = s.1291,
    #         BB_1292 = s.1292,
    #         BB_1293 = s.1293,
    #         BB_1294 = s.1294,
    #         BB_1295 = s.1295,
    #         BB_1296 = s.1296,
    #         BB_1297 = s.1297,
    #         BB_1298 = s.1298,
    #         BB_1308 = s.1308,
    #         BB_1309 = s.1309,
    #         BB_1310 = s.1310,
    #         BB_1374 = s.1374,
    #         BB_1415 = s.1415,
    #         BB_1439 = s.1439,
    #         BB_1441 = s.1441,
    #         BB_1443 = s.1443,
    #         BB_1486 = s.1486,
    #         BB_1487 = s.1487,
    #         BB_1489 = s.1489,
    #         BB_1490 = s.1490,
    #         BB_1491 = s.1491,
    #         BB_1494 = s.1494,
    #         BB_1495 = s.1495,
    #         BB_1497 = s.1497,
    #         BB_1499 = s.1499,
    #         BB_1500 = s.1500,
    #         BB_1501 = s.1501,
    #         BB_1502 = s.1502,
    #         BB_1503 = s.1503,
    #         BB_1504 = s.1504,
    #         BB_1505 = s.1505,
    #         BB_1506 = s.1506,
    #         BB_1507 = s.1507,
    #         BB_1508 = s.1508,
    #         BB_1510 = s.1510,
    #         BB_1511 = s.1511,
    #         BB_1512 = s.1512,
    #         BB_1513 = s.1513,
    #         BB_1514 = s.1514,
    #         BB_1515 = s.1515,
    #         BB_1516 = s.1516,
    #         BB_1517 = s.1517,
    #         BB_1518 = s.1518,
    #         BB_1519 = s.1519,
    #         BB_1521 = s.1521,
    #         BB_1524 = s.1524,
    #         BB_1526 = s.1526,
    #         BB_1527 = s.1527,
    #         BB_1530 = s.1530,
    #         BB_1531 = s.1531,
    #         BB_1532 = s.1532,
    #         BB_1533 = s.1533,
    #         BB_1534 = s.1534,
    #         BB_1535 = s.1535,
    #         BB_1536 = s.1536,
    #         BB_1537 = s.1537,
    #         BB_1539 = s.1539,
    #         BB_1540 = s.1540,
    #         BB_1541 = s.1541,
    #         BB_1542 = s.1542,
    #         BB_1543 = s.1543,
    #         BB_1544 = s.1544,
    #         BB_1545 = s.1545,
    #         BB_1546 = s.1546,
    #         BB_1547 = s.1547,
    #         BB_1548 = s.1548,
    #         BB_1549 = s.1549,
    #         BB_1550 = s.1550,
    #         BB_1551 = s.1551,
    #         BB_1552 = s.1552,
    #         BB_1553 = s.1553,
    #         BB_1554 = s.1554,
    #         BB_1555 = s.1555,
    #         BB_1556 = s.1556,
    #         BB_1557 = s.1557,
    #         BB_1558 = s.1558,
    #         BB_1561 = s.1561,
    #         BB_1562 = s.1562,
    #         BB_1563 = s.1563,
    #         BB_1564 = s.1564,
    #         BB_1572 = s.1572,
    #         BB_1573 = s.1573,
    #         BB_1574 = s.1574,
    #         BB_1576 = s.1576,
    #         BB_1577 = s.1577,
    #         BB_1581 = s.1581,
    #         BB_1601 = s.1601)

    #     db.session.add(sample)
    #     db.session.commit()

def loadMetaD():
    csv = "static/assets/resources/data/belly_button_metadata.csv"
    MetaD_df = pd.read_csv(csv, encoding='utf-8')
    MetaD_df.to_sql(name='metad', con=engine, if_exists = 'replace', index=True)

# Build database from models
@app.before_first_request
def build():
    #Drop existing DB
    db.drop_all()
    #Rebuild DB and tables from models
    db.create_all()
    #Load the tables with data from csv files
    loadSamples()
    loadMetaD()

#================================
#   Routes
#================================

#Root
@app.route("/")
def dashboard():
    return "HomePage"
    # return render_template("index.html")

#

if __name__ == '__main__':
    app.run(debug=True)