from pydantic import BaseModel
from typing import Optional

class NewsResponse(BaseModel):
    id: int
    message_id: Optional[int]
    title: str
    text: str
    photo: Optional[str]
    reg_date: str

    class Config:
        from_attributes = True