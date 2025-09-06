from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    def __repr__(self):
        return (
            f"<Student(id={self.id}, "
            f"name={self.first_name} {self.last_name}, "
            f"email={self.email})>"
        )


# Добавляем новые модели для SQL запросов
class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return f"<User(user_id={self.user_id}, email={self.user_email})>"


class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String(100), nullable=False)
    description = Column(String(200))
    credits = Column(Integer, default=3)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return (
            f"<Subject(subject_id={self.subject_id}, "
            f"title={self.subject_title})>"
        )


class StudentEducation(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    education_form = Column(String(50), nullable=False)
    enrollment_year = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    def __repr__(self):
        return (
            f"<StudentEducation(student_id={self.student_id}, "
            f"user_id={self.user_id}, form={self.education_form})>"
        )
