# Generated by Django 4.2.3 on 2023-07-24 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_user_followers_user_following_post_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
