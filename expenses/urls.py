from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from .views import AmountValidationView, DescriptionValidationView

urlpatterns = [
    path('', views.index, name="expenses"),
    path('my-expense', views.expense_my, name="my-expenses"),
    path('add-expense', views.add_expense, name="add-expenses"),
    path('edit-expense/<int:id>', views.expense_edit, name="expense-edit"),
    path('expense-delete/<int:id>', views.delete_expense, name="expense-delete"),
    path('expense_category_summary', views.expense_category_summary, name='expense_category_summary'),
    path('validate-amount', csrf_exempt(AmountValidationView.as_view()), name='validate-amount'),
    path('validate-desc', csrf_exempt(DescriptionValidationView.as_view()), name='validate-desc'),
    path('stats', views.stats_view, name='stats')
]
