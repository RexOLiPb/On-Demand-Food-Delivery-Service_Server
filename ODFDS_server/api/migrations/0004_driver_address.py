# Generated by Django 2.1.7 on 2019-04-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190429_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]