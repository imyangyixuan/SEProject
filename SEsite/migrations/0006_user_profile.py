# Generated by Django 3.0 on 2019-12-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEsite', '0005_remove_user_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile',
            field=models.TextField(default='', verbose_name='profile'),
        ),
    ]
