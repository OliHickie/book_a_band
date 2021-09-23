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
    name = models.CharField(max_length=24, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=False,
                                 blank=False)
    location = models.CharField(max_length=18, null=False, blank=False)
    image_one = models.ImageField(null=True, blank=True)
    image_two = models.ImageField(null=True, blank=True)
    image_three = models.ImageField(null=True, blank=True)
    image_four = models.ImageField(null=True, blank=True)
    biography = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name


class BandReview(models.Model):

    band = models.ForeignKey('Band', null=True, blank=True, on_delete=models.CASCADE)
    author = models.CharField(max_length=50, null=False, blank=False)
    review = models.TextField(null=False, blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author
