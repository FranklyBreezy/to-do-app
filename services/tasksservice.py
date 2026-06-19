from schemas.tasks import tasks_create , tasks_update
from uuid import UUID, uuid4
from datetime import datetime , timezone
from sqlalchemy.orm import Session
from models import Task
from fastapi import HTTPException , status
def create_resource(data : tasks_create , db : Session):
    # id = str(uuid4())
    # created_at = datetime.utcnow()
    # while id in db:
    #     id = uuid4()
    # id , as in Task.id is now generated via the db layer, as defined in the models.py file
     t_d = Task(**data.model_dump())
    #  The ** operator "unpacks" a dictionary into keyword arguments.
     db.add(t_d)
     db.commit()
     db.refresh(t_d)
    # t_d["id"] = id
    # t_d["created_at"] = created_at
    # t_d["updated_at"] = created_at
     return t_d

def read_all(db : Session):
    # return db.items()
    tasks_list = db.query(Task).all()
    if not tasks_list:
        return []
    return tasks_list
    # funnily enough I actually forgot to write the code for return the tasks_list even if it did exist xD

def update_resource(id : str, data : tasks_update,db:Session):
    # t_data = db.get(id)
    # updates = data.model_dump(exclude_unset=True)
    # t_data.update(updates)
    # updated_at = datetime.utcnow()
    # t_data["updated_at"] = updated_at
    # db[id] = t_data
    # return db[id]
    t_d = db.query(Task).filter(Task.id == id).first()
    if t_d is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Task resource not found")
    update = data.model_dump(exclude_unset=True)
    for field , val in update.items():
        setattr(t_d,field,val)
    db.commit()
    db.refresh(t_d)
    return t_d

def delete_resource(id : str,db:Session):
    # db.pop(id)
    # return {"deletion":"successful"}
    task = db.query(Task).filter(Task.id == id).first()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task resource not found")
    db.delete(task)
    db.commit()
    return {"message":"Task deleted successfully"}