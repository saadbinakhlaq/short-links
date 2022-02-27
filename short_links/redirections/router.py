from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from short_links import db
from short_links.links.models import Link
from short_links.links.services import get_link_and_update_click

router = APIRouter(tags=['Redirections'], prefix='')

@router.get('/{short_link_id}', status_code=status.HTTP_307_TEMPORARY_REDIRECT)
async def handle_redirection(short_link_id: str, database: Session = Depends(db.get_db)):
    link = await get_link_and_update_click(short_link_id, database)
    return RedirectResponse(url=link.original_url)
    