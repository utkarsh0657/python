from fastapi import FastAPI
from app.routers import upload, status, webhook

app = FastAPI()

app.include_router(upload.router)
app.include_router(status.router)
app.include_router(webhook.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Image Processing API"}
