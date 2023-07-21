# Noted-FastAPI
This is a REST API for a note-taking service. This was built to demonstrate how to use FastAPI with Async SQLAlchemy and PostgreSQL
[Video here](https://youtu.be/nC9ob8xM3AM)

## How to run the code
- Create a ```DATABASE_URL``` variable in a ```.env``` file. This must be a Postgresql database URI.
- Install all project requirements from the ```requirements.txt``` file using ```pip install -r requirements.txt```
- Create the database by running ``` python create_db ```
- Finally run your server with ```uvicorn main:app```

Please star this repo
