import pytest

@pytest.mark.django_db
def test_welcome_django(client):
    """
    Asserts whether the base URL 200s

    200 means that the HTTP request was successful and 
    that the frontpage exists.
    """
    response = client.get("http://localhost:8000/")
    assert response.status_code == 200

