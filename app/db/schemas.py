from pydantic import BaseModel
from datetime import date

class TripBase(BaseModel):
    destination: str
    start_date: date
    end_date: date

class TripCreate(BaseModel):
    start_date: str
    end_date: str
    destination: str

class TripResponse(TripBase):
    id: int

class Config:
    orm_mode = True
