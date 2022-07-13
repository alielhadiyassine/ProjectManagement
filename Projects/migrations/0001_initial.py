# Generated by Django 3.2rc1 on 2021-04-13 23:25

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
                ('projID', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
