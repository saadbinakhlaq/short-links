from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from short_links import db

from . import schema
from . import services
from . import validator

router = APIRouter(tags=['Links'], prefix='/api/v1/links')

@router.post('', status_code=status.HTTP_201_CREATED)
async def create_short_links(request: schema.Link, database: Session = Depends(db.get_db)):
    if request.expiration_date:
        if not validator.verify_expiration_date(request.expiration_date):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Expiration date should be greater than current time"
            )
    new_link = await services.create_new_links(request.original_url, database)
    return { "short_link": f"tier.app/{new_link.short_link_id}" }