# Generated by Django 4.2.4 on 2023-08-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload', models.FileField(upload_to='uploads/')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=50)),
                ('link', models.CharField(max_length=100)),
                ('deploy', models.CharField(max_length=100)),
                ('project', models.CharField(max_length=100)),
            ],
        ),
    ]