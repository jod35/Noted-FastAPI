from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker
from schemas import NoteModel, NoteCreateModel
from models import Note
from typing import List
from crud import CRUD
from db import engine
import uuid

app = FastAPI(docs_url="/", title="Note Taking API")


session = async_sessionmaker(bind=engine, expire_on_commit=False)

db = CRUD(session)


@app.get("/notes", response_model=List[NoteModel])
async def list_all_notes():
    """List all notes"""
    notes = await db.get_all()
    return notes


@app.post(
    "/notes",
    response_model=NoteCreateModel,
)
async def create_note(note: NoteCreateModel):
    """Create a note"""
    note_obj = Note(id=str(uuid.uuid4()), title=note.title, content=note.content)

    await db.insert_objects(note_obj)

    return note_obj


@app.get("/note/{note_id}")
async def get_note(note_id: str):
    """Get note by id"""

    note = await db.retrieve_item(note_id)

    return note


@app.put("/note/{note_id}")
async def update_note(note_id: str, note_data: NoteCreateModel):
    """Update note by id"""

    result = await db.update_item(
        note_id, {"title": note_data.title, "content": note_data.content}
    )

    return result


@app.delete("/note/{note_id}", status_code=204)
async def delete_note(note_id: str):
    """Delete Note"""

    note = await db.delete_item(note_id)

    return {}
