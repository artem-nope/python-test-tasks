# uvicorn main:app --reload
from fastapi import FastAPI
import sqlite3
import datetime
from pydantic import BaseModel
from typing import List


class LanguageItem(BaseModel):
    id: int
    name: str
    year: int
    rating: float
    created: datetime.datetime


class LanguageCreate(BaseModel):
    name: str
    year: int
    rating: float


class LanguageUpdate(BaseModel):
    rating: float


class ResponseItem(BaseModel):
    message: str


app = FastAPI()
DB = 'db3.sqlite3'


@app.get("/", response_model=List[LanguageItem])
async def root():
    with sqlite3.connect(DB, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        data = [dict(item) for item in cursor.execute('SELECT * FROM languages')]
        return data


@app.get("/{lan_id}/", response_model=LanguageItem)
async def get_language(lan_id: int):
    with sqlite3.connect(DB, check_same_thread=False) as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        data = dict(cursor.execute('SELECT * FROM languages WHERE id = ?', [lan_id]).fetchone())
        return data


@app.post("/create/", response_model=ResponseItem)
async def create_language(item: LanguageCreate):
    with sqlite3.connect(DB, check_same_thread=False) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO languages(name, year, rating, created) VALUES(?, ?, ?, DATETIME("now"))',
                           [item.name, item.year, item.rating])
            connection.commit()
        except Exception as e:
            print(e)
        else:
            return {
                'message': 'Added new language'
            }


@app.delete("/delete/{lan_id}/", response_model=ResponseItem)
async def delete_language(lan_id: int):
    with sqlite3.connect(DB, check_same_thread=False) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM languages WHERE id = ?', [lan_id])
            connection.commit()
        except Exception as e:
            print(e)
        else:
            return {
                'message': 'Deleted one language'
            }


@app.put("/update/{lan_id}/", response_model=ResponseItem)
async def update_language(lan_id: int, item: LanguageUpdate):
    with sqlite3.connect(DB, check_same_thread=False) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute('UPDATE languages SET rating = ? WHERE id = ?', [item.rating, lan_id])
            connection.commit()
        except Exception as e:
            print(e)
        else:
            return {
                'message': 'Updated one language'
            }