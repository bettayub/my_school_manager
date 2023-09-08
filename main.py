# main.py
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Course, Enrollment, Base, engine

# Create database tables if they don't exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
