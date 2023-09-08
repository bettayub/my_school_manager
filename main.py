# main.py
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Course, Enrollment, Base, engine

# Create database tables if they don't exist
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


# Function to register a new student
def register_student():
    print("Student Registration")
    name = input("Enter student's name: ")
    adm = input("Enter admission number: ")
    # Create a new student instance and add it to the session
    student = Student(student_name=name, student_adm=adm, student_fee_balance=0)
    session.add(student)
    session.commit()
    print(f"Registered student: {name}, Admission Number: {adm}")

