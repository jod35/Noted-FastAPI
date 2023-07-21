from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from crud import CRUD
from db import engine
from schemas import NoteModel, NoteCreateModel
from http import HTTPStatus
from typing import List
from models import Note
import uuid

app = FastAPI(
    title="Noted API", description="This is a simple note taking service", docs_url="/"
)


session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD()


@app.get("/notes", response_model=List[NoteModel])
async def get_all_notes():
    notes = await db.get_all(session)

    return notes


@app.post("/notes", status_code=HTTPStatus.CREATED)
async def create_note(note_data: NoteCreateModel):
    new_note = Note(
        id=str(uuid.uuid4()), title=note_data.title, content=note_data.content
    )

    note = await db.add(session, new_note)

    return note


@app.get("/note/{note_id}")
async def get_note_by_id(note_id):
    note = await db.get_by_id(session, note_id)

    return note


@app.patch("/note/{note_id}")
async def update_note(note_id: str, data: NoteCreateModel):
    note = await db.update(
        session, note_id, data={"title": data.title, "content": data.content}
    )

    return note


@app.delete("/note/{note_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_note(note_id):
    note = await db.get_by_id(session, note_id)

    result = await db.delete(session, note)

    return result
