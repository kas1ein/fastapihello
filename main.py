from fastapi import FastAPI, Query
import os

app = FastAPI()

@app.get("/")
async def read_root(name: str = Query(default="World", description="The name to greet")):
    data_folder = "data"
    data_file = "data.txt"
    file_path = os.path.join(data_folder, data_file)

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            file_content = file.read()
        return {"message": f"Hello there, {name}. {file_content}"}
    else:
        return {"message": f"Hello there, {name}. File not found."}
