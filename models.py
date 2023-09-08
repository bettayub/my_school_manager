
# Import necessary modules and create the SQLAlchemy engine and base.

# models.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Create the SQLAlchemy base and engine for the SQLite database.
Base = declarative_base()
engine = create_engine('sqlite:///school.db')


# Define the Student class for the 'students' table.
class Student(Base):
    __tablename__ = 'students'

    # Define columns for student information.
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_adm = Column(String)
    student_academics = Column(Integer)
    student_attendance = Column(Float)
    
    # Add the student_fee_balance column.
    student_fee_balance = Column(Integer)

    # Define relationships with other tables.
    parent_id = Column(Integer, ForeignKey('parents.parent_id'))
    teacher_id = Column(Integer, ForeignKey('teachers.teacher_id'))
    parent = relationship('Parent', back_populates='students')
    teacher = relationship('Teacher', back_populates='students')
    fees = relationship('Fee', back_populates='student')
    enrollments = relationship('Enrollment', back_populates='student')
    courses = relationship('Course', secondary='enrollments', back_populates='students')
