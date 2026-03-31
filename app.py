# =========================================
# Dumela App - Main Application Entry Point
# =========================================

from flask import Flask, request, redirect
from auth_middleware import require_auth

app = Flask(__name__)


# -----------------------------------------
# Force HTTPS
# -----------------------------------------
@app.before_request
def force_https():
    if request.headers.get("X-Forwarded-Proto", "http") != "https":
        return redirect(request.url.replace("http://", "https://", 1))


# -----------------------------------------
# Security Headers
# -----------------------------------------
@app.after_request
def set_security_headers(response):
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    return response


# -----------------------------------------
# Root Route (Health Check / Base Route)
# -----------------------------------------
@app.route("/")
def home():
    return "Dumela App Running"


# -----------------------------------------
# Example Protected Route
# -----------------------------------------
@app.route("/dashboard")
@require_auth()
def dashboard():
    return "Dashboard - Authenticated"


# -----------------------------------------
# Run App
# -----------------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)