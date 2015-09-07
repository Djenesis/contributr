import pytest

from django.core.urlresolvers import reverse
from contriblog.models import Post

@pytest.mark.django_db
def test_call_blog(client):
    """
    Asserts whether the blog page sends a 200 HTTP status code as response

    200 means that the HTTP request was successful. The URL and port
    may vary. The fixture above the function allows the function to
    access the database.
    """
    response = client.get(reverse("blog:index"))
    assert response.status_code == 200

@pytest.mark.django_db
def test_call_blog_subpage(client):
    """
    Asserts whether subpages of the blog page 404

    404 means that no page is returned. This is the expected behaviour,
    because we don't have subpages for the blog at the moment.
    """
    response = client.get(reverse("blog:index") + "december")
    assert response.status_code == 404

@pytest.mark.django_db
def test_string_representation(client):
    """
    Asserts wether the blog post string representation (__str__) is equal 
    to the blog title.
    """
    post = Post(title="Test title blog")
    assert str(post) == "Test title blog"
