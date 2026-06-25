import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_get_single_user(api_client):
    response = api_client.get_user(2)
    body = response.json()

    assert response.status_code == 200
    assert "data" in body
    assert "support" in body
    assert body["data"]["id"] == 2
    assert body["data"]["email"] == "janet.weaver@reqres.in"
    assert isinstance(body["data"]["first_name"], str)
    assert isinstance(body["data"]["last_name"], str)
    assert body["data"]["avatar"].startswith("https://")
