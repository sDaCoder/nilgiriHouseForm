from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="views")

def getTemp(request: Request):
    return templates.TemplateResponse(
        request = request,
        name = "form.html.jinja"
    )