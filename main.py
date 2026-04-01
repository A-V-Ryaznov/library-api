from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}


def run() -> None:
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8282,
        log_level="trace"
    )

if __name__ == "__main__":
    run()