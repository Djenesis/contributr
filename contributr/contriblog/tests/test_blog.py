import pytest

from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
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
def test_blog_model():
    """
    Create a user and a blog post with publish set to false.
    Then assert that number of blog posts equals 1.
    """
    user = get_user_model().objects.create(username="bloghero")
    post = Post(title="Test title blog", author=user,
                body="Blogging here!", publish=False)
    post.save()
    assert Post.objects.all().count() == 1

    """
    Assert that the custom queryset displays posts that has publish
    set to true.
    """
    assert Post.objects.published().count() == 0
    post.publish = True
    post.save()
    assert Post.objects.published().count() == 1

    """
    Asserts wether the post string representation (__str__) is equal
    to the blog title.
    """
    assert str(post) == "Test title blog"
