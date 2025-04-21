from fastapi import FastAPI
from app.database import engine
from app.routes import example  

app = FastAPI()

app.include_router(example.router)

@app.get("/")
async def root():
    return {"message": "Cloud Service Access Management System API"}
