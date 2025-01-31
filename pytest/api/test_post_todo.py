import pytest
import random
from playwright.sync_api import APIRequestContext, Playwright
from typing import Generator

# In testing, a fixture provides a defined, reliable and consistent context for the tests.
# We may configure "FUNCTION" scope & "SESSION" scope.

@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="http://localhost:3000"
    )
    yield request_context
    # This method discards all stored responses
    request_context.dispose()

# Test the POST request for creating a new todo item
def test_post_todo(api_request_context: APIRequestContext) -> None:
    # Dettagli estratti dalla richiesta POST nel file HAR
    endpoint = "/todos"

    # Generate a random 10-digit ID starting with 0
    random_id = f"0{random.randint(100000000, 999999999)}"

    payload = {
        "title": "pee",
        "completed": False,
        "id": random_id  # Use the dynamically generated ID
    }

    # Eseguire la richiesta POST
    response = api_request_context.post(endpoint, data=payload)

    # Verificare che la richiesta abbia avuto successo
    assert response.status == 201, f"Expected status 201, got {response.status}"
    response_body = response.json()
    
    # Verificare i dati restituiti
    assert response_body["title"] == payload["title"]
    assert response_body["completed"] == payload["completed"]
    assert response_body["id"] == payload["id"]