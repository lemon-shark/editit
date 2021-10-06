from django.contrib import admin
from .models import Expense, Category
from import_export.admin import ImportExportModelAdmin

# admin.site.register(Expense)
admin.site.register(Category)


@admin.register(Expense)
class ExpenseAdmin(ImportExportModelAdmin):
    pass
