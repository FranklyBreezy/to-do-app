from fastapi import APIRouter , HTTPException, Depends
from schemas.tasks import tasks_return , tasks_create , tasks_update
from services.tasksservice import create_resource , read_all , delete_resource , update_resource
from uuid import UUID
from services.db_dependency import get_db
from sqlalchemy.orm import Session
tasks = APIRouter(
    tags=["tasks"],
    prefix="/tasks"
)

@tasks.get("/")
def get_all(db : Session = Depends(get_db)):
    try:
        return read_all(db)
    except HTTPException:
        raise

@tasks.post("/",response_model=tasks_return)
async def create_task(data:tasks_create,db : Session = Depends(get_db)):
    try:
        return create_resource(data,db)
    except HTTPException:
        raise

@tasks.put("/{task_id}",response_model=tasks_return)
async def update_task(task_id , data : tasks_update,db : Session = Depends(get_db)):
    try:
        return update_resource(task_id,data,db)
    except HTTPException:
        raise

@tasks.delete("/{task_id}")
def delete_task(task_id,db:Session = Depends(get_db)):
    try:    
        return delete_resource(task_id,db)
    except HTTPException:
        raise