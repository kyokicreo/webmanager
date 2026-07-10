from fastapi import FastAPI
from app.database import engine, Base
from app import models
from app.routers import auth, files, history

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(files.router, prefix="/files", tags=["Files"])
app.include_router(history.router, prefix="/history", tags=["History"])


@app.get("/")
def read_root():
    return {"message": "FastAPI работает!"}