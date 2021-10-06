from django.contrib import admin
from .models import Account, School, Level
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Account)
admin.site.register(School)
admin.site.register(Level)


@admin.register(Account)
class AccountAdmin(ImportExportModelAdmin):
    pass
