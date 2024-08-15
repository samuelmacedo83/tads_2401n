import pytest
import sqlite3
import os
import sys 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions.create_db import create_db

def test_create_db():

    conn = create_db('test')

    # Check if the returned object is a valid sqlite3.Connection instance
    assert isinstance(conn, sqlite3.Connection)

    # Check if the file has been created
    assert os.path.exists("test.db")

    # Clean up
    conn.close()
    os.remove("test.db")
