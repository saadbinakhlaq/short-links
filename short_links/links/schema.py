from pydantic import BaseModel, AnyHttpUrl
from datetime import date, datetime
from typing import Optional


class Link(BaseModel):
    original_url: AnyHttpUrl
    expiration_date: Optional[datetime]

