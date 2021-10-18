from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings
import csv
from django.http import HttpResponse
from io import StringIO
from django.contrib import admin
from csvexport.actions import csvexport


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField(default="Null")
    #     owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.CharField(max_length=266)

    def __str__(self):
        return self.category

    class Meta:
        ordering = ['-date']


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class StatAdmin(admin.ModelAdmin):
    actions = [csvexport]
    # list_display = ('amount', 'date', 'description', 'owner', 'category')
    #
    # def download_csv(self, request, queryset):
    #     f = StringIO.StringIO()
    #     writer = csv.writer(f)
    #     writer.writerow(["amount", "date", "description", "owner", "category"])
    #
    #     for s in queryset:
    #         writer.writerow([s.code, s.country, s.ip, s.url, s.count])
    #
    #     f.seek(0)
    #     response = HttpResponse(f, content_type='text/csv')
    #     response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
    #     return response
    #
    # download_csv.short_description = "Download CSV file for selected stats."
