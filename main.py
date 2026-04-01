from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn

app = FastAPI()

@app.get("/health")
def health_check():
    return Response(status_code=200)








def run() -> None:
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=8282,
        log_level="trace"
    )

if __name__ == "__main__":
    run()