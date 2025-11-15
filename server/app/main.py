from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Welcome to the server application!")

@app.route('/report-status')
def report_status():
    return jsonify(status="Server is running")

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)