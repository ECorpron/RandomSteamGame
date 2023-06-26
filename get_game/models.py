from django.db import models


# Create your models here.
class Account(models.Model):
    profile_id = models.IntegerField()

    def __str__(self):
        return self.profile_id
