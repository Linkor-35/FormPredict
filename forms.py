from pydantic import BaseModel
from datetime import datetime


class IsValidForm(BaseModel):
    id: int
    email: str
    date: datetime
    text: str