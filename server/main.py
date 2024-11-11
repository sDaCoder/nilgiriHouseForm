from fastapi import FastAPI, Request
import uvicorn
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

@app.api_route("/", methods=["GET", "POST"])
def root(req: Request, item: Feedback):
    if req.method == 'GET':
        greet()

    elif req.method == 'POST':
        postFeedback(item)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=80, reload=True)