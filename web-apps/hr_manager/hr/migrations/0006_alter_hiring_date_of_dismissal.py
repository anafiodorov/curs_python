# Generated by Django 4.2.1 on 2023-05-19 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0005_rename_id_employee_hiring_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiring',
            name='date_of_dismissal',
            field=models.DateField(null=True),
        ),
    ]
