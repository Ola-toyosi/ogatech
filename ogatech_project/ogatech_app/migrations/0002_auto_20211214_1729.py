# Generated by Django 3.0.14 on 2021-12-14 16:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ogatech_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ogatech_app_UserProfileInfo',
            new_name='UserProfileInfo',
        ),
    ]