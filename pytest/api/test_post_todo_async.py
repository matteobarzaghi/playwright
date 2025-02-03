import random
import pytest
from playwright.async_api import async_playwright

@pytest.mark.asyncio
async def test_post_todo_async():
    async with async_playwright() as playwright:
        api_request_context = await playwright.request.new_context(base_url="http://localhost:3000")

        # Generate a random 10-digit ID starting with 0
        random_id = f"0{random.randint(100000000, 999999999)}"

        data = {
            "completed": False,
            "title": "test",
            "id": random_id  # Use the dynamically generated ID
        }

        response = await api_request_context.post("/todos", data=data)

        assert response.ok, f"Failed to create todo: {response.status} - {await response.text()}"
        print(f"Response: {await response.text()}")
