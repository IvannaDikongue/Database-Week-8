from sqlalchemy.orm import Session
from database import SessionLocal
from models import User, Task, UserCreate, TaskCreate, TaskUpdate

def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(Username=user.Username, Email=user.Email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_all_tasks():
    db = SessionLocal()
    return db.query(Task).all()

def create_task(task: TaskCreate):
    db = SessionLocal()
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(task_id: int, task: TaskUpdate):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.TaskID == task_id).first()
    if db_task:
        for key, value in task.dict().items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    return {"error": "Task not found"}

def delete_task(task_id: int):
    db = SessionLocal()
    db_task = db.query(Task).filter(Task.TaskID == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return {"message": "Task deleted"}
    return {"error": "Task not found"}
