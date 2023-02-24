from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/api/words")
def get_list_of_words():
    return { "value": "ABC" }
