from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import select
from models import Note



class CRUD:
    def __init__(self,async_session:async_sessionmaker[AsyncSession]):
        self.session = async_session()

    async def insert_objects(self, note: Note):
        self.session.add(note)
        await self.session.commit()
        return note


    async def get_all(self):
        statement = select(Note).order_by("created_at")
        result = await self.session.execute(statement)
        return result.scalars()


    async def retrieve_item(self,note_id:str):
        statement = select(Note).filter(Note.id == note_id)
        result = await self.session.execute(statement)
        return result.scalars().one()
        
    async def update_item(self,note_id:str,data:dict):
        result = await self.retrieve_item(note_id)
        result.title = data['title']
        result.content = data['content']
        await self.session.commit()
        return result 

    async def delete_item(self,note_id):
        result = await self.retrieve_item(note_id)
        await self.session.delete(result)
        return result