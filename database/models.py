from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import datetime

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    department_id = Column(Integer, primary_key=True)
    department_name = Column(String(100), unique=True, nullable=False)
    
    students = relationship("Student", back_populates="department")
    faculty = relationship("Faculty", back_populates="department")
    classes = relationship("Class", back_populates="department")

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False) # Student, Faculty, Parent, HOD, Principal, Admin
    phone = Column(String(20))
    bio = Column(Text, default="Academic enthusiast and active learner.")
    
    student_profile = relationship("Student", back_populates="user", uselist=False)
    faculty_profile = relationship("Faculty", back_populates="user", uselist=False)
    leave_applications = relationship("LeaveApplication", back_populates="user")

class Student(Base):
    __tablename__ = 'students'
    student_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    enrollment_no = Column(String(50), unique=True, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    semester = Column(Integer, nullable=False)
    section = Column(String(10), nullable=False)
    
    user = relationship("User", back_populates="student_profile")
    department = relationship("Department", back_populates="students")
    attendance_records = relationship("Attendance", back_populates="student")

class Faculty(Base):
    __tablename__ = 'faculty'
    faculty_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    
    user = relationship("User", back_populates="faculty_profile")
    department = relationship("Department", back_populates="faculty")
    sessions = relationship("AttendanceSession", back_populates="faculty")

class Subject(Base):
    __tablename__ = 'subjects'
    subject_id = Column(Integer, primary_key=True)
    subject_code = Column(String(20), unique=True, nullable=False)
    subject_name = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    
    sessions = relationship("AttendanceSession", back_populates="subject")

class Class(Base):
    __tablename__ = 'classes'
    class_id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('departments.department_id'))
    semester = Column(Integer, nullable=False)
    section = Column(String(10), nullable=False)
    
    department = relationship("Department", back_populates="classes")
    sessions = relationship("AttendanceSession", back_populates="class_group")

class FacultySubject(Base):
    __tablename__ = 'faculty_subject'
    mapping_id = Column(Integer, primary_key=True)
    faculty_id = Column(Integer, ForeignKey('faculty.faculty_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    class_id = Column(Integer, ForeignKey('classes.class_id'))

class AttendanceSession(Base):
    __tablename__ = 'attendance_sessions'
    session_id = Column(Integer, primary_key=True)
    faculty_id = Column(Integer, ForeignKey('faculty.faculty_id'))
    subject_id = Column(Integer, ForeignKey('subjects.subject_id'))
    class_id = Column(Integer, ForeignKey('classes.class_id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    expires_at = Column(DateTime, nullable=False)
    qr_token = Column(String(255), unique=True, nullable=False)
    
    faculty = relationship("Faculty", back_populates="sessions")
    subject = relationship("Subject", back_populates="sessions")
    class_group = relationship("Class", back_populates="sessions")
    attendance_records = relationship("Attendance", back_populates="session")

class Attendance(Base):
    __tablename__ = 'attendance'
    attendance_id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey('attendance_sessions.session_id'))
    student_id = Column(Integer, ForeignKey('students.student_id'))
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String(20), default="PRESENT") # PRESENT, LATE, ABSENT
    verification_method = Column(String(50), default="QR_SCAN")
    
    session = relationship("AttendanceSession", back_populates="attendance_records")
    student = relationship("Student", back_populates="attendance_records")

class LeaveApplication(Base):
    __tablename__ = 'leave_applications'
    leave_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    applicant_name = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
    from_date = Column(String(20), nullable=False)
    to_date = Column(String(20), nullable=False)
    reason = Column(Text, nullable=False)
    status = Column(String(20), default="Pending") # Pending, Approved, Rejected
    applied_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    user = relationship("User", back_populates="leave_applications")

# Database Engine & Session Factory Setup
engine = create_engine('sqlite:///pragyan_ai.db', echo=False)
SessionLocal = sessionmaker(bind=engine)

def init_db():
    """Initializes and creates all database tables."""
    Base.metadata.create_all(engine)
