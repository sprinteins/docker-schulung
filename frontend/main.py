from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})