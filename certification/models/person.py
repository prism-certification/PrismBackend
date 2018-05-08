from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100)
    github_user_name = models.CharField(max_length=100)
    linkedin_vanity_name = models.CharField(max_length=50)
    stackoverflow_id = models.IntegerField()
