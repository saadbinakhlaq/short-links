from webbrowser import get
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from short_links import db
from short_links.links.services import get_link_by_short_link_id

router = APIRouter(tags=['Stats'], prefix='/stats')

@router.get('', status_code=status.HTTP_200_OK)
async def get_short_link_stats(short_link_id: str, database: Session = Depends(db.get_db)):
    link = await get_link_by_short_link_id(short_link_id, database)
    return { "clicks": link.stat.clicks }
    