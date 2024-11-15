from fastapi import APIRouter, Request, UploadFile, File
from controllers.postDataControl import post_file

postDataRouter = APIRouter()

@postDataRouter.post('/')
def root(request: Request, file: UploadFile = File(...)):
    return post_file(request=request, file=file)