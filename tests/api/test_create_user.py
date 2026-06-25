import pytest


@pytest.mark.api
@pytest.mark.regression
def test_create_user(api_client):
    payload = {"name": "Juan QA", "job": "Automation Engineer"}

    response = api_client.create_user(payload)
    body = response.json()

    assert response.status_code == 201
    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    assert "id" in body and body["id"]
    assert "createdAt" in body and body["createdAt"]
