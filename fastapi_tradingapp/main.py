from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
def get_hello():
    return 'Hello World!'


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("fastapi_tradingapp.main:app", host="0.0.0.0", port=8000, reload=True)
