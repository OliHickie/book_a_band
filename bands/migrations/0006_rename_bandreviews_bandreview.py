# Generated by Django 3.2.6 on 2021-09-23 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0005_bandreviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BandReviews',
            new_name='BandReview',
        ),
    ]
