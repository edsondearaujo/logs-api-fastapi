from fastapi import FastAPI, Depends, HTTPException
from . import crud, models, schemas
from .database import SessionLocal, engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/logs/", response_model=schemas.Log)
def create_log(log: schemas.LogCreate, db: Session = Depends(get_db)):
    return crud.create_log(db=db, log=log)

@app.get("/logs/", response_model=list[schemas.Log])
def read_logs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logs = crud.get_logs(db, skip=skip, limit=limit)
    return logs