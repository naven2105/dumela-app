"""
File: app.py
Path: F:\Projects\dumela-app\app.py

Purpose:
- Dumela App (with auth protection)
"""

from flask import Flask
from auth_middleware import require_auth

app = Flask(__name__)


@app.route("/")
@require_auth()
def home():
    return "Dumela App Running (Authenticated)"


if __name__ == "__main__":
    app.run(port=5001, debug=True)