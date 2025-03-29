from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, Sai Krishna Kalluri. How is life! I am assuming it is wonderful!!"}