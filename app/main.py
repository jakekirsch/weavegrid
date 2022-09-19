from fastapi import FastAPI

from app.routes.routes import router


app: FastAPI = FastAPI()
app.include_router(router)
