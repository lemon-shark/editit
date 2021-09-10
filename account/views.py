# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
#
# from expenses.models import Category, Expense
#
#
# @login_required(login_url='/authentication/loginnew')
# def my_account(request):
#     categories = Category.objects.all()
#     expenses = Expense.objects.filter(owner=request.user)
#
#     context = {
#         'expenses': expenses,
#     }
#     return render(request, 'my-account.html', context)
from django.http import HttpResponse


def my_account(request):
    return HttpResponse("Account app works!")
