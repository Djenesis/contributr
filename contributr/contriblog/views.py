from django.views import generic

from . import models


# Generic view that lists all blog posts that has publish set to true.
class BlogIndex(generic.ListView):
    queryset = models.Post.objects.published()
    template_name = "contriblog/index.html"


# Generic view that displays each post.
class BlogDetail(generic.DetailView):
    model = models.Post
    template_name = "contriblog/detail.html"

# Generic view that lists every post with selected tag.
class TagDetail(generic.DetailView):
    model = models.Tag
    template_name = "contriblog/tag.html"
    slug_url_kwarg = "tag"
