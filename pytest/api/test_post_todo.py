import pytest
import random
from playwright.sync_api import APIRequestContext, Playwright
from typing import Generator

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="module")
def todo_id() -> str:
    """Generates and shares a random todo ID between tests"""
    return f"0{random.randint(100000000, 999999999)}"

def test_post_todo(api_request_context: APIRequestContext, todo_id: str) -> None:
    """Test creating a new todo item."""
    endpoint = "/todos"

    payload = {
        "title": "Walk the dog",
        "completed": False,
        "id": todo_id  # Use the dynamically generated ID
    }

    response = api_request_context.post(endpoint, data=payload)

    assert response.status == 201, f"Expected status 201, got {response.status}"
    response_body = response.json()

    assert response_body["title"] == payload["title"]
    assert response_body["completed"] == payload["completed"]
    assert response_body["id"] == payload["id"]

def test_complete_todo(api_request_context: APIRequestContext, todo_id: str) -> None:
    """Test updating a todo item to mark it as completed."""
    endpoint = f"/todos/{todo_id}"

    update_payload = {
        "title": "Walk the dog",
        "completed": True,  # Updating this field
        "id": todo_id
    }

    response = api_request_context.put(endpoint, data=update_payload)

    assert response.status == 200, f"Expected status 200, got {response.status}"
    response_body = response.json()

    assert response_body["completed"] is True, "Todo item should be marked as completed"
    assert response_body["id"] == todo_id
