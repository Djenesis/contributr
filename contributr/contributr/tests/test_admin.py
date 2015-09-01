import pytest

@pytest.mark.django_db
def test_welcome_django(admin_client):
    """
    Asserts whether the admin page sends a 200 HTTP status code as response

    200 means that the HTTP request was successful. Tests for the admin
    pages are done with the admin_client. The URL and port may vary. The
    fixture above the function allows the function to access the database.
    """
    response = admin_client.get("http://localhost:8000/admin/")
    assert response.status_code == 200

