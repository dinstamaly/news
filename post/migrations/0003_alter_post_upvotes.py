# Generated by Django 3.2.8 on 2021-10-30 06:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_rename_author_name_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upvotes',
            field=models.ManyToManyField(blank=True, related_name='votes', to=settings.AUTH_USER_MODEL),
        ),
    ]
