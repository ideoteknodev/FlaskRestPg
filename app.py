from flask import Flask, request
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env file into environment

url = os.environ.get("DATABASE_URL")
connection = psycopg2.connect(url)
app = Flask(__name__)

@app.get("/")
def index():
    return {"message": "Hellow World"}
@app.get("/detail/<string:room>")
def detail(room):
    return {"message": room}