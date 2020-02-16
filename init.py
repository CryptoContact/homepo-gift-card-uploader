from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://homepoor_userV2:I3f@NPtdCo1*%Y3kck5$@96.127.186.10/homepoor_v2'
db = SQLAlchemy(app)