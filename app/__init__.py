from distutils.log import Log
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Modelo Pydantic para os logs
class LogCreate(BaseModel):
    timestamp: datetime
    level: str
    message: str
    source: str

# Endpoint para receber logs
@app.post("/logs/")
async def create_log(log: LogCreate):
    db = next(get_db())
    db_log = Log(**log.model_dump())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return {"message": "Log recebido com sucesso!", "log_id": db_log.id}

# Endpoint para consultar logs
@app.get("/logs/")
async def get_logs(level: str = None, source: str = None):
    db = next(get_db())
    query = db.query(Log)
    if level:
        query = query.filter(Log.level == level)
    if source:
        query = query.filter(Log.source == source)
    logs = query.all()
    return {"logs": logs}