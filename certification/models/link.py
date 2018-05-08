from django.db import models
from django.core.validators import URLValidator
from . import Company, Person


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=256)
    field = models.URLField(max_length=2048, validators=[URLValidator()])
