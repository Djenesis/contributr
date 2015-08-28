import pytest

@pytest.mark.django_db
def test_welcome_django(client):
    """
    Asserts whether the base URL 404s

    404 means that the HTTP request could not reach a page. We don't have a
    page yet, so 404 is the expected return.
    """
    response = client.get("http://localhost:8000/")
    assert response.status_code == 404

