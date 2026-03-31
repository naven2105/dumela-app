"""
File: db.py
Path: F:\\Projects\\dumela-app\\db.py

Purpose:
- Database connection handler
"""

import os
import psycopg2


def get_db_connection():
    return psycopg2.connect(os.environ["DATABASE_URL"])