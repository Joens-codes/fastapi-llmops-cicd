from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "Week2 Day4 CI/CD demo app"}

@app.get("/health")
def health():
    return {"ok": True}
