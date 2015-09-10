from django.db import models

from django.core.urlresolvers import reverse


# Custom queryset manager that only displays posts that have publish set to true.
class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)

    objects = PostQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"
        ordering = ["-created_date"]
