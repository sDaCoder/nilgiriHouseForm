from fastapi import Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from pathlib import Path
import datetime
import shutil

templates = Jinja2Templates(directory="views")

UPLOAD_DIR = "uploads"
Path(UPLOAD_DIR).mkdir(parents=True, exist_ok=True)

def post_file(request: Request, file: UploadFile = File(...)):
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_location = f"{UPLOAD_DIR}/{timestamp}_{file.filename}"

    print(f"Saving file to: {file_location}")

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return templates.TemplateResponse(
        "form.html.jinja",
        {"request": request, "filename": file.filename, "location": file_location}
    )