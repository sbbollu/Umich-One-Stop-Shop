from pydantic import BaseModel
import datetime

class Review(BaseModel):
    location: str
    rating: int
    review: str
    date: datetime



