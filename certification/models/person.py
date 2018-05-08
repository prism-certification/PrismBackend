from django.db import models
from . import Company


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    companies = models.ManyToManyField(Company)
