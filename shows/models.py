from django.db import models

from django.utils.timezone import now

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["name"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        if len(postData['release_date']) < 8:
            errors["release_date"] = "Show release date should a valid date"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255, default="")
    release_date = models.DateField(default=now)
    desc = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)