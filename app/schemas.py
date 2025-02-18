from pydantic import BaseModel
from datetime import datetime

class LogBase(BaseModel):
    timestamp: datetime
    level: str
    message: str
    source: str

class LogCreate(LogBase):
    pass

class Log(LogBase):
    id: int

    class Config:
        from_attributes = True