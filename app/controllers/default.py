from app import app
from flask import Flask, jsonify
from app.config import get_db_connection
from app.controllers import usuario 

@app.route('/')
def index():
    return 'Hello, World!'
