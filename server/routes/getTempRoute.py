from fastapi import APIRouter, Request
from controllers.getTempControl import getTemp

getTemplateRouter = APIRouter()

@getTemplateRouter.get('/')
def root(request: Request):
    return getTemp(request=request)