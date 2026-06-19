# TO-DO-API (FastAPI + SQLAlchemy + SQLite)

A backend API for managing tasks using FastAPI.
It uses SQLAlchemy ORM with SQLite for data storage and is containerized using Docker.

---
## Features
- CRUD
- SQLAlchemy ORM for database operations
- SQLite for data persistence
- Docker and Docker Compose setups
- Volume mounting for data persistence across container restarts

---
### TECH STACK
- FastAPI
- SQLite
- SQLAlchemy
- Docker and Docker Compose
- Pydantic
---
#### HOW TO RUN LOCALLY
- Clone the repo : ```git clon <url>```
- CD into the folder : ```cd to-do-app```
- ```docker compose up --build```
- ```docker compose down```
- Alternatively you can do :
- ```pip install -r requirements.txt```
- ```uvicorn main:app --reload```
- It will be accessiblee at ```http://127.0.0.1:8000```
