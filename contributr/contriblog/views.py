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
