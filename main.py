from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
task_id_counter = 1


class Task(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def root():
    return {"message": "Tasker API is running!"}

#Get 1 all tasks

@app.get("/tasks")
def get_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not Found")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/tasks")
def create_task(task: Task):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "completed": task.completed
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task