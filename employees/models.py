from django.db import models


class Employee(models.Model):
    emp_id = models.CharField(max_length=10, unique=True)
    emp_name = models.CharField(max_length=100)
    emp_email = models.EmailField(unique=True)
    emp_phone = models.CharField(max_length=15, unique=True)
    emp_department = models.CharField(max_length=50)    

    def __str__(self):
        return self.emp_name