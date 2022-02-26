import base64
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from typing import Optional
import hashlib

from sqlalchemy.orm import Session

from . import models


def generate_unique_short_link_id(link: str):
    link_to_encode = f"{link}:{datetime.now().strftime('%s')}"
    sha256_string = hashlib.sha256(link_to_encode.encode()).digest()
    short_link_id = base64.urlsafe_b64encode(sha256_string).decode()
    return short_link_id[:8]

async def create_new_links(original_url: str, database: Session) -> models.Link:
    short_link_id = generate_unique_short_link_id(original_url)
    new_link = models.Link(
      short_link_id=short_link_id,
      original_url=original_url,
      expiration_date=datetime.now() + timedelta(days=30)
    )
    database.add(new_link)
    database.commit()
    database.refresh(new_link)
    return new_link

async def get_link_by_short_link_id(short_link_id: str, database: Session) -> Optional[models.Link]:
    link = database.query(models.Link).filter_by(short_link_id=short_link_id).first()
    if link is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return link