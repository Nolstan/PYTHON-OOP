from fastapi import FastAPI
from .database import engine, Base
from . import models
from .schemas import blog

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post('/blog')
def create_blog(request: blog):
    return request


