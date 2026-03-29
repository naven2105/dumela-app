"""
File: db.py
Path: F:\Projects\dumela-app\db.py

Purpose:
- Database connection (uses environment variable)
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_db_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])