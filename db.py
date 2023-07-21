from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
import os


load_dotenv()


#engine object to connect to db
engine = create_async_engine(
    url= os.getenv('DATABASE_URL'),
    echo = True
)


#base class for creating database models
class Base(DeclarativeBase):
    pass
