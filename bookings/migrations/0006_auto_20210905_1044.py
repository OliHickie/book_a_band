# Generated by Django 3.2.6 on 2021-09-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0005_newbooking_band_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='newbooking',
            name='price',
            field=models.IntegerField(default=1800),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newbooking',
            name='band_name',
            field=models.CharField(max_length=50),
        ),
    ]
