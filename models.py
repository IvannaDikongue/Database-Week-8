from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Text, Enum, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "Users"
    UserID = Column(Integer, primary_key=True, index=True)
    Username = Column(String(50), unique=True, nullable=False)
    Email = Column(String(100), unique=True, nullable=False)

class Task(Base):
    __tablename__ = "Tasks"
    TaskID = Column(Integer, primary_key=True, index=True)
    UserID = Column(Integer, ForeignKey("Users.UserID"), nullable=False)
    Title = Column(String(100), nullable=False)
    Description = Column(Text)
    Status = Column(Enum("Pending", "In Progress", "Completed"), default="Pending")
    DueDate = Column(Date)

# Pydantic models
class UserCreate(BaseModel):
    Username: str
    Email: str

class TaskCreate(BaseModel):
    UserID: int
    Title: str
    Description: str = ""
    Status: str = "Pending"
    DueDate: str

class TaskUpdate(BaseModel):
    Title: str
    Description: str
    Status: str
    DueDate: str
