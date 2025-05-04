from fastapi import FastAPI, HTTPException
from database import SessionLocal
import crud
import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Task Manager API"}

@app.post("/users/")
def create_user(user: models.UserCreate):
    return crud.create_user(user)

@app.get("/tasks/")
def get_tasks():
    return crud.get_all_tasks()

@app.post("/tasks/")
def create_task(task: models.TaskCreate):
    return crud.create_task(task)

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: models.TaskUpdate):
    return crud.update_task(task_id, task)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    return crud.delete_task(task_id)
