from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .db import Base


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    department = Column(String)

class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    job = Column(String)

class HiredEmployee(Base):
    __tablename__ = 'hired_employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    datetime = Column(DateTime)
    department_id = Column(Integer, ForeignKey('departments.id'))
    job_id = Column(Integer, ForeignKey('jobs.id'))

    # Define the relationships with Department and Job models
    department = relationship("Department", backref="hired_employees")
    job = relationship("Job", backref="hired_employees")