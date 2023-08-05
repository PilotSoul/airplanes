from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=1024)
    plane = models.ForeignKey('Plane', on_delete=models.PROTECT, null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Plane(models.Model):
    model = models.CharField(max_length=100, db_index=True)
    description = models.CharField(max_length=1024)

    def __str__(self):
        return self.model