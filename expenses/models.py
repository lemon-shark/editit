from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField(default="Null")
    #     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=266)
    kind = models.BooleanField(default=False)

    def __str__(self):
        return self.category

    class Meta:
        ordering: ['-date']


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
