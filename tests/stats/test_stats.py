from asyncio import base_events
from datetime import timedelta
import pytest

from httpx import AsyncClient
from datetime import datetime, timedelta
from conf_test_db import app, override_get_db

from short_links.links.models import Link, Stat
from short_links.links.services import generate_unique_short_link_id


@pytest.mark.asyncio
async def test_stats_for_link_in_db():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        database = next(override_get_db())
        original_url = "http://www.actual_url_2.com"
        short_link_id = generate_unique_short_link_id(original_url)
        new_link = Link(
          original_url=original_url,
          short_link_id=short_link_id,
          expiration_date=datetime.now() + timedelta(days=10)
        )
        stat = Stat(link=new_link)
        database.add(new_link)
        database.add(stat)
        database.commit()
        database.refresh(new_link)

        url = f"/stats?short_link_id={new_link.short_link_id}"
        response = await ac.get(url)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_stats_for_link_not_in_db():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        url = f"/stats?short_link_id=random_link"
        response = await ac.get(url)
    assert response.status_code == 404
