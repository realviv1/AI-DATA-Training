from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from the World"}

@app.get("/home/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}"}