from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "deployed on vercel"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
