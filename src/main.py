from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def index():
    return {"message": "hello world!"}


def start():
    """
    Launched with `poetry run dev` at root level
    :return: None
    """
    uvicorn.run("src.main:app", host="0.0.0.0", port=8880, reload=True)
