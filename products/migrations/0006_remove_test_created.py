# Generated by Django 3.1.7 on 2021-06-06 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_test_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='created',
        ),
    ]