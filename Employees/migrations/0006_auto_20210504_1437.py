# Generated by Django 3.2rc1 on 2021-05-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employees', '0005_employee_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='Image',
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.CharField(default='', max_length=20),
        ),
    ]
