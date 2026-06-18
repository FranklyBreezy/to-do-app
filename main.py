from fastapi import FastAPI
from routers.tasksrouter import tasks
app = FastAPI()
app.include_router(tasks)
@app.get("/")
def root():
    return {"service":"is live!"}