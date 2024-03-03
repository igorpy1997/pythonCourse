# Generated by Django 4.2.4 on 2023-08-07 14:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog_app", "0002_alter_customuser_options_alter_customuser_groups_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                related_name="liked_posts",
                through="blog_app.Like",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
