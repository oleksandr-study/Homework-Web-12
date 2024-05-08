from fastapi import FastAPI

from src.routes import contacts
from src.routes import auth

app = FastAPI()

app.include_router(auth.router)
app.include_router(contacts.router)


@app.get("/")
def main_root():
    return {"message": "Contacts application"}