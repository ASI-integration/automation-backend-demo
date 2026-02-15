from fastapi import FastAPI
from app.routers.users import router as users_router
from app.logger import logger

app = FastAPI()

app.include_router(users_router)

@app.get("/")
def root():
    logger.info("Health check called")
    return {"status": "ok"}
