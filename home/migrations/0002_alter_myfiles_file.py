# Generated by Django 4.1.5 on 2023-01-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myfiles',
            name='file',
            field=models.ImageField(upload_to='media'),
        ),
    ]
