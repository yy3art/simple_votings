# Generated by Django 5.0.1 on 2024-01-27 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Landing', '0003_user_delete_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
