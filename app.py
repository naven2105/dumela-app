"""
File: app.py
Path: /app.py

Purpose:
- Dumela App (initial setup)
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Dumela App Running"


if __name__ == "__main__":
    app.run(port=5001, debug=True)
    