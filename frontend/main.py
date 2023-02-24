from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_index(request: Request):
    response = requests.get("http://localhost:3000/api/words")
    words = response.json()

    context = {
        "request": request,
        "data":  words,
    }
    return templates.TemplateResponse("index.html", context)