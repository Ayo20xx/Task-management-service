from fastapi import FastAPI

app=FastAPI()

task={}
task_id=1

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/tasks")
async def new_task(title:str):
    global task_id

    task={
        "id": task_id,
        "title": title,
        "completed": False
    }
    task[task_id]= task
    task_id += 1
    return task

@app.get("/tasks")
async def view():
    return task

@app.get("/tasks/{id}")
async def indvidual(id:int):
    task=task.get(id)
    if task:
        return task
    return {"error":"task not found" }



@app.delete("/tasks/{id}")
async def delete_task(id: int):
    if id in task:
       deleted = task.pop(id)
       return {"message": "Task deleted", "task": deleted}

    return {"error": "Task not found"}
    
@app.patch("/tasks/{task_id}")
async def complete_task(task_id: int):

    task = task.get(task_id)

    if task:
        task["completed"] = True
        return task

    return {"error": "Task not found"}