# Generated by Django 4.2.4 on 2023-08-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload',
            field=models.CharField(max_length=150),
        ),
    ]
