from django.utils import timezone
from django.db import models
from . import Person


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField()
    persons = models.ManyToManyField(Person)
    github_organization_name = models.CharField(max_length=100)
    linkedin_vanity_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Company, self).save(*args, **kwargs)
