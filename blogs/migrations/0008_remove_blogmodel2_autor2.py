# Generated by Django 4.0.4 on 2022-06-24 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_blogmodel2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogmodel2',
            name='autor2',
        ),
    ]
