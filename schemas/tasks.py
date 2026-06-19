from pydantic import BaseModel
from datetime import datetime 
from typing import Optional
class tasks(BaseModel):
    title : str
    description: Optional[str] = None

class tasks_create(tasks):
    pass

class tasks_return(tasks):
    id : str
    created_at: datetime
    updated_at : datetime

class tasks_update(BaseModel):
    title : Optional[str] = None
    description: Optional[str] = None