# Generated by Django 3.0 on 2019-12-22 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SEsite', '0008_auto_20191222_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='creator',
            field=models.EmailField(default='', max_length=254, verbose_name='email'),
        ),
    ]
