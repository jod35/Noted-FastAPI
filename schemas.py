from pydantic import BaseModel, ConfigDict
from datetime import datetime


#schema for returning a note
class NoteModel(BaseModel):

    id : str
    title :str
    content: str
    date_created : datetime

    model_config = ConfigDict(
        from_attributes= True
    )


#schema for creating a note
class NoteCreateModel(BaseModel):
    title :str
    content: str

    model_config = ConfigDict(
        from_attributes= True,
        json_schema_extra={
            "example":{
                "title":"Sample title",
                "content" : "Sample content"
            }
        }
    )
