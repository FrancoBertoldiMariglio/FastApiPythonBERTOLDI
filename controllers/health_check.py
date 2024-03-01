from fastapi import APIRouter
from config.database import Database

router = APIRouter()
db = Database()


@router.get("/")
def health_check():
    if db.check_connection():
        return {"status": "OK"}

    return {"status": "ERROR"}
