from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "ok"}
