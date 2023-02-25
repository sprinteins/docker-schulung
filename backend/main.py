from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel
from db import engine, WordsDB
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

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

path = "/api/words"

# Declare paths
@app.get(path)
def get_list_of_words():
    word_list = []
    with engine.connect() as conn:
        result = conn.execute(WordsDB.select())
        for row in result:
            word_list.append({ "word": row.word, "length": row.length })
            
    return word_list

@app.post(path, status_code=201)
def add_word_to_list(words: Words):
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            for item in words.list:
                lower_case = item.lower()
                # Lookup if word is existing
                stmt = select(WordsDB).where(WordsDB.c.word == lower_case)
                result = conn.execute(stmt)

                # Insert if not existing
                if result.fetchone() is None:
                    conn.execute(WordsDB.insert().values(word=lower_case, length=len(lower_case)))
                
            trans.commit()
        except IntegrityError as e:
            print("Error: ", e)
            trans.rollback()
    return