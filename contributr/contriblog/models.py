from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey('auth.User')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
