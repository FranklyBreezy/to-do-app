from fastapi import FastAPI
from routers.tasksrouter import tasks
from models import Base
from db import engine
app = FastAPI()
app.include_router(tasks)
Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"service":"is live!"}