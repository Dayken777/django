# Generated by Django 4.0.1 on 2022-01-09 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
