# Generated by Django 3.0 on 2019-12-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='fromWho',
            field=models.CharField(max_length=18, verbose_name='fromWho'),
        ),
    ]
