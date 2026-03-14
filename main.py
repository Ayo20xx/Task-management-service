from fastapi import FastAPI
from pydantic import BaseModel




app=FastAPI()

class TaskCreate(BaseModel):
    title:str


tasks={}
task_id=1

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/tasks")
async def new_task(task:TaskCreate):
    """
    Create new task
    """
    global task_id

    task={
        "id": task_id,
        "title": task.title,
        "completed": False
    }
    tasks[task_id]= new_task
    task_id += 1
    return new_task

@app.get("/tasks")
async def get_task():
    return tasks

@app.get("/tasks/{id}")
async def get_task(id:int):
    task=tasks.get(id)
    if task:
        return task
    return {"error":"task not found" }



@app.delete("/tasks/{id}")
async def delete_task(id: int):
    if id in tasks:
       deleted = tasks.pop(id)
       return {"message": "Task deleted", "task": deleted}

    return {"error": "Task not found"}
    
@app.patch("/tasks/{task_id}")
async def complete_task(task_id: int):

    task = tasks.get(task_id)

    if task:
        task["completed"] = True
        return task

    return {"error": "Task not found"}