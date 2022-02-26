from asyncio import base_events
import pytest

from httpx import AsyncClient
from conf_test_db import app


@pytest.mark.asyncio
async def test_create_short_links_with_correct_data():
    data = {
        "original_url": "http://www.actual_url.com",
        "expiration_date": "2024-08-26T14:15:22Z"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/links", json=data)
    assert response.status_code == 201

@pytest.mark.asyncio
async def test_create_short_links_with_incorrect_original_url():
    data = {
        "original_url": "asd",
        "expiration_date": "2019-08-26T14:15:22Z"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/links", json=data)
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_create_short_links_with_expiration_date_less_than_current():
    data = {
        "original_url": "asd",
        "expiration_date": "2019-08-26T14:15:22Z"
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/links", json=data)
    assert response.status_code == 422