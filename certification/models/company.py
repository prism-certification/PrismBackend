from django.db import models
from . import Person, Link


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    persons = models.ManyToManyField(Person)
    github_organization_name = models.CharField(max_length=100)
    linkedin_vanity_name = models.CharField(max_length=50)
