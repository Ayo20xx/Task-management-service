from fastapi import FastAPI, HTTPException, status
from schema import TaskCreate,TaskResponse

app = FastAPI()



tasks = {
    1: {"id": 1, "title": "Buy groceries", "completed": False},
    2: {"id": 2, "title": "Finish report", "completed": True},
}

current_id = 3


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/tasks", response_model=TaskResponse)
async def new_task(task: TaskCreate):
    global current_id

    new_task = {
        "id": current_id,
        "title": task.title,
        "completed": False
    }

    tasks[current_id] = new_task
    current_id += 1

    return new_task


@app.get("/tasks", response_model=list[TaskResponse])
async def get_all_tasks():
    return list(tasks.values())


@app.get("/tasks/{task_id}", response_model=TaskResponse)
async def get_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    return task


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    tasks.pop(task_id)
    return {"message": "Task deleted"}


@app.patch("/tasks/{task_id}", response_model=TaskResponse)
async def complete_task(task_id: int):
    task = tasks.get(task_id)

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )

    task["completed"] = True
    return task