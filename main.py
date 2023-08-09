from fastapi import FastAPI
import models
from db import engine
import user


app = FastAPI()
app.include_router(user.router)

@app.get('/')
def first_page():
    return 'Welcome'

models.Base.metadata.create_all(engine) #-> database creation