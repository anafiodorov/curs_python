# Generated by Django 4.2.1 on 2023-05-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=255, unique=True)),
                ('last_name', models.CharField(max_length=255, unique=True)),
                ('salary', models.IntegerField()),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
