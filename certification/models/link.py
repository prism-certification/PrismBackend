from django.db import models
from django.utils import timezone
from django.core.validators import URLValidator
from . import Company, Person


class Link(models.Model):
    id = models.BigAutoField(primary_key=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT)
    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.PROTECT)
    description = models.CharField(max_length=256)
    field = models.URLField(max_length=2048, validators=[URLValidator()])
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Link, self).save(*args, **kwargs)
