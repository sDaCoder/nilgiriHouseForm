from fastapi import FastAPI
import uvicorn
from routes.getTempRoute import getTemplateRouter
from routes.postDataRoute import postDataRouter

app = FastAPI()

app.include_router(router = getTemplateRouter)
app.include_router(router = postDataRouter)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, reload=True)