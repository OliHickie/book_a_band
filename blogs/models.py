from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    author = models.CharField(max_length=30, null=False, blank=False)
    source = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
