# StayAutomated

Demo backend automation system.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- JWT Auth
- Docker

## Goal
Showcase backend architecture, authentication, and CRUD patterns.

Work in progress.
## Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload
## Run with Docker

docker build -t automation-backend-demo .
docker run -p 8000:8000 automation-backend-demo
