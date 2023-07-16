from pydantic import BaseModel, Field
import secrets


class NoteModel(BaseModel):
    id: str
    title: str
    content: str

    model_config = {"from_attributes": True}


class NoteCreateModel(BaseModel):
    title: str
    content: str

    model_config = {
        "json_schema_extra": {
            "example": {"title": "a test title", "content": "content for a note"}
        },
        "from_attributes": True,
    }
