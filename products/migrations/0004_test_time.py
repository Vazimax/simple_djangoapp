# Generated by Django 3.1.7 on 2021-06-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
