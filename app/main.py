from fastapi import FastAPI, Response
from app.api.base import api_router
import uvicorn

app = FastAPI()
app.include_router(api_router)


@app.get('/')
async def read_taxes(response: Response):

    return {"Hello World": "My API"}


def start():
    uvicorn.run(app, port=8001, log_level="debug")

if __name__ == "__main__":
    start()