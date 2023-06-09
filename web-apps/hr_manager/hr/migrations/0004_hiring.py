# Generated by Django 4.2.1 on 2023-05-19 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_alter_employee_first_name_alter_employee_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hiring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_of_employment', models.DateField()),
                ('date_of_dismissal', models.DateField()),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.employee')),
                ('id_employer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hr.employer')),
            ],
            options={
                'db_table': 'hirings',
            },
        ),
    ]
