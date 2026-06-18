from fastapi import APIRouter , HTTPException , status
from schemas.tasks import tasks_return , tasks_create , tasks_update
from services.tasksservice import create_resource , read_all , delete_resource , update_resource
from uuid import UUID
tasks = APIRouter(
    tags=["tasks"],
    prefix="/tasks"
)

@tasks.get("/",)
def get_all():
    try:
        return read_all()
    except Exception as e:
        raise

@tasks.post("/",response_model=tasks_return)
async def create_task(data:tasks_create):
    try:
        return create_resource(data)
    except Exception as e:
        raise

@tasks.put("/{task_id}",response_model=tasks_return)
async def update_task(task_id , data : tasks_update):
    try:
        return update_resource(task_id,data)
    except Exception as e:
        raise

@tasks.delete("/{task_id}")
def delete_task(task_id ):
    try:    
        return delete_resource(task_id)
    except Exception as e:
        raise