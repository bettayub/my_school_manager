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


# Function to add academic marks for a student (Teacher)
def add_academics():
    print("Add Academics")
    student_id = int(input("Enter student ID: "))
    student = session.query(Student).filter_by(student_id=student_id).first()
    
    if not student:
        print("Student not found.")
        return

    marks = int(input("Enter academic marks: "))
    # Update the student's academic marks and commit the changes
    student.student_academics = marks
    session.commit()
    print(f"Academic marks added for {student.student_name}: {marks}")


