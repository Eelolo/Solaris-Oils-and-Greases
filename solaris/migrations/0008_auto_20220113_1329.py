# Generated by Django 3.2.11 on 2022-01-13 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solaris', '0007_auto_20220113_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='catalog_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='nav_page',
            field=models.BooleanField(default=False),
        ),
    ]
