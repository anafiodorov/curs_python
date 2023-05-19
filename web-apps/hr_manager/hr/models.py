from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, unique=True, null=False)


class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    salary = models.IntegerField(null=False)


class Hiring(models.Model):
    class Meta:
        db_table = 'hirings'

    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    employer = models.ForeignKey(Employer, on_delete=models.DO_NOTHING)
    date_of_employment = models.DateField(null=False)
    date_of_dismissal = models.DateField(null=True)
