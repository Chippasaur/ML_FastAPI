import uvicorn
from fastapi import FastAPI

# init app
app = FastAPI()


# Routes
@app.get('/')
async def index():
    return {"text": "Hello Worlds"}
