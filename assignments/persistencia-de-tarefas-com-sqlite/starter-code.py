from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel, Field

app = FastAPI(title="API de Tarefas")


class TaskInput(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    concluida: bool = False


class Task(TaskInput):
    id: int


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/")
def home():
    return {"mensagem": "API de tarefas funcionando!"}


@app.post("/tarefas", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task_input: TaskInput):
    global next_task_id
    task = Task(id=next_task_id, **task_input.model_dump())
    tasks[next_task_id] = task
    next_task_id += 1
    return task


@app.get("/tarefas", response_model=list[Task])
def list_tasks():
    return list(tasks.values())


@app.get("/tarefas/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return task


@app.put("/tarefas/{task_id}", response_model=Task)
def update_task(task_id: int, task_input: TaskInput):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    task = Task(id=task_id, **task_input.model_dump())
    tasks[task_id] = task
    return task


@app.delete("/tarefas/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    del tasks[task_id]
    return Response(status_code=status.HTTP_204_NO_CONTENT)