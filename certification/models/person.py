from django.utils import timezone
from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    birthday = models.DateField()
    github_user_name = models.CharField(max_length=100)
    linkedin_vanity_name = models.CharField(max_length=50)
    stackoverflow_id = models.IntegerField()
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Person, self).save(*args, **kwargs)
