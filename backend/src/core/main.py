from fastapi import FastAPI, status

app = FastAPI()


@app.get("/health", status_code=status.HTTP_200_OK)
def health() -> dict:
    return {"status": "ok"}


@app.get("/", status_code=status.HTTP_200_OK)
def home() -> dict:
    return {"status": "ok"}
