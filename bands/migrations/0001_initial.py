# Generated by Django 3.2.6 on 2021-08-13 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('friendly_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('tagline', models.CharField(blank=True, max_length=100)),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=30)),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_three', models.ImageField(blank=True, null=True, upload_to='')),
                ('biography', models.TextField()),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='bands.category')),
            ],
        ),
    ]
