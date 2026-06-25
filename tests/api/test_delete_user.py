import pytest


@pytest.mark.api
@pytest.mark.regression
def test_delete_user(api_client):
    response = api_client.delete_user(2)

    assert response.status_code == 204
    assert response.text == ""
