
# Import necessary modules and create the SQLAlchemy engine and base.

# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy base and engine for the SQLite database.
Base = declarative_base()
engine = create_engine('sqlite:///school.db')

