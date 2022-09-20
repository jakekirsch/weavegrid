from fastapi import FastAPI

from app.routes import routes


app: FastAPI = FastAPI()
app.include_router(routes.router)
