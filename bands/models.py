from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Band(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=24)
    price = models.IntegerField()
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    location = models.CharField(max_length=18)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    image_four = models.ImageField(null=True, blank=True)
    biography = models.TextField()


    def __str__(self):
        return self.name
