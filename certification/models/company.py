from django.db import models
from . import Person


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    persons = models.ManyToManyField(Person)
