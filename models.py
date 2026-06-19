from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column , String, Integer , DateTime
from uuid import uuid4
from datetime import datetime
class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id =  Column(
       String,
       primary_key = True,
       default=lambda : str(uuid4())
    )

    title = Column(
        String,
        nullable = False
    )

    description = Column(
        String
    )

    created_at = Column(
        DateTime,
        default = datetime.utcnow
    )

    updated_at = Column(
        DateTime,
        default = datetime.utcnow,
        onupdate = datetime.utcnow
    )

