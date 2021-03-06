# Generated by Django 3.1.7 on 2021-06-06 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=100)),
                ('config', models.TextField(max_length=9999)),
                ('price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('image', models.ImageField(upload_to='images/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
