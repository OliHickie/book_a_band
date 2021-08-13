from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    friendly_name = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Band(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    tagline = models.CharField(max_length=100, blank=True)
    price = models.IntegerField()
    location = models.CharField(max_length=30)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    biography = models.TextField()

    def __str__(self):
        return self.name
