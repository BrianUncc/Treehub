# Generated by Django 5.1.1 on 2024-11-17 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_userprofile_concentration_userprofile_goal1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
