from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

# Testing
word_list = []

# Classes
class Words(BaseModel):
    list: List[str]

# FastAPI Initialization
origins = ["http://localhost:8080"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

path = "/api/words"

# Declare paths
@app.get(path)
def get_list_of_words():
    return word_list

@app.post(path)
def add_word_to_list(words: Words):
    for word in words.list:
        word_list.append({ "word": word, "length": len(word) })
    return