# StayAutomated

Demo backend automation system.

## Tech Stack
- Python
- FastAPI
- PostgreSQL
- JWT Auth
- Docker

## Goal
## Goal
Demonstrate a production-style backend with authentication, CRUD, and clean architecture patterns.
## Run locally

pip install -r requirements.txt
uvicorn app.main:app --reload
## Run with Docker

docker build -t automation-backend-demo .
docker run -p 8000:8000 automation-backend-demo
✅ CI/CD with GitHub Actions  
Automatic dependency install and import test on every push.
![CI](https://github.com/ASI-integration/automation-backend-demo/actions/workflows/main.yml/badge.svg)
