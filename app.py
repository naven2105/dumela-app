# =========================================
# Dumela App - Main Application Entry Point
# =========================================

from flask import Flask
from auth_middleware import auth_required

app = Flask(__name__)


# -----------------------------------------
# Root Route (Health Check / Base Route)
# -----------------------------------------
@app.route("/")
def home():
    return "Dumela App Running"


# -----------------------------------------
# Example Protected Route (keep existing)
# -----------------------------------------
@app.route("/dashboard")
@auth_required
def dashboard():
    return "Dashboard - Authenticated"


# -----------------------------------------
# Run App
# -----------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)