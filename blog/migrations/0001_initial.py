# Generated by Django 4.1.4 on 2022-12-12 03:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('decription', models.TextField()),
                ('image', models.ImageField(upload_to='blog/images')),
                ('date', models.DateField(verbose_name=datetime.date.today)),
            ],
        ),
    ]
