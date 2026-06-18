from schemas.tasks import tasks_create , tasks_update
from db import db
from uuid import UUID, uuid4
from datetime import datetime , timezone
def create_resource(data : tasks_create):
    id = str(uuid4())
    created_at = datetime.utcnow()
    while id in db:
        id = uuid4()
    t_d = data.model_dump()
    t_d["id"] = id
    t_d["created_at"] = created_at
    t_d["updated_at"] = created_at
    db[id] = t_d
    return db[id]

def read_all():
    return db.items()

def update_resource(id : str, data : tasks_update):
    t_data = db.get(id)
    updates = data.model_dump(exclude_unset=True)
    t_data.update(updates)
    updated_at = datetime.utcnow()
    t_data["updated_at"] = updated_at
    db[id] = t_data
    return db[id]

def delete_resource(id : str):
    db.pop(id)
    return {"deletion":"successful"}