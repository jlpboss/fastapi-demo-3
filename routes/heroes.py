from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
from database import SessionLocal
import schemas
from crud import get_heros_v1, get_heros

router = APIRouter(
    prefix="/heroes"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/all", response_model=List[schemas.HeroModel])
def get_heroes(db: Session = Depends(get_db)):
    heroes =  get_heros(db)
    return heroes
