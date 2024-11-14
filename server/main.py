from fastapi import FastAPI, Request, UploadFile, File
import uvicorn
from fastapi.templating import Jinja2Templates

import datetime
import shutil
from pathlib import Path
from models.feedback import Feedback

app = FastAPI()

def greet():
    return {"message": "Hello World"}

def postFeedback(item: Feedback):
    dic = {
        "status": "Success",
        "message": "Feedback is successfully posted",
        "feedback": item.dict()
    }
    print(dic)
    return dic

templates = Jinja2Templates(directory="views")

@app.get("/")
def rootG():
    return greet()

@app.post("/")
def rootP(req: Request, item: Feedback):
    return postFeedback(item)

UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

@app.post("/upload/")
async def post_file(file: UploadFile = File(...)):
    # Format the timestamp to avoid invalid characters in the filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_location = f"{UPLOAD_DIR}/{timestamp}_{file.filename}"

    # Optional: print the file location to verify the path
    print(f"Saving file to: {file_location}")

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "location": file_location}

@app.get("/upload/")
def getTemp(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "form.html.jinja"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, reload=True)