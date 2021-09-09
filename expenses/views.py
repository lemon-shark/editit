from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Expense
from django.contrib import messages
from django.core.paginator import Paginator
import datetime
import re
from django.views import View
import json
from django.http import JsonResponse


@login_required(login_url='/authentication/loginnew')
def index(request):
    categoties = Category.objects.all()
    context = {
        'categories': categoties,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        # kind = request.POST['kind']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)

        if not re.match(r'^[1-9]\d*$', amount):
            messages.error(request, 'Please enter a positive amount')
            return render(request, 'expenses/add_expense.html', context)

        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', context)

        Expense.objects.create(owner=request.user, amount=amount, date=date, category=category, description=description)
        # ,kind=kind)
        messages.success(request, 'Expense saved successfully')
        return redirect('my-expenses')


def expense_my(request):
    categories = Category.objects.all()
    expenses = Expense.objects.filter(owner=request.user)
    paginator = Paginator(expenses, 5)
    page_number = request.GET.get('page')
    page_obj = Paginator.get_page(paginator, page_number)

    context = {
        'expenses': expenses,
        'page_obj': page_obj
    }
    return render(request, 'expenses/my-expense.html', context)


def add_expense(request):
    categoties = Category.objects.all()
    context = {
        'categories': categoties,
        'values': request.POST
    }

    if request.method == 'GET':
        return render(request, 'expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        # kind = request.POST['kind']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/add_expense.html', context)

        # if not re.match(r'^[1-9]\d*$', amount):
        #     messages.error(request, 'Please enter a positive amount')
        #     return render(request, 'expenses/add_expense.html', context)

        if not date:
            messages.error(request, 'Date is required')
            return render(request, 'expenses/add_expense.html', context)

        Expense.objects.create(owner=request.user, amount=amount, date=date, category=category, description=description)
        # ,kind=kind)
        messages.success(request, 'Expense saved successfully')
        return redirect('my-expenses')


def expense_edit(request, id):
    categories = Category.objects.all()
    expense = Expense.objects.get(pk=id)
    context = {
        'expense': expense,
        'values': expense,
        'categories': categories,
    }
    if request.method == 'GET':
        return render(request, 'expenses/edit-expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']
        # kind = request.POST['kind']

        if not amount:
            messages.error(request, 'Amount is required')
            return render(request, 'expenses/edit_expense.html', context)

        if not description:
            messages.error(request, 'Description is required')
            return render(request, 'expenses/edit_expense.html', context)

        expense.owner = request.user
        expense.amount = amount
        expense.date = date
        expense.category = category
        expense.description = description

        expense.save()
        messages.success(request, 'Expense updated successfully')
        return redirect('my-expenses')


def delete_expense(request, id):
    expense = Expense.objects.get(pk=id)
    expense.delete()
    messages.success(request, 'Expense removed')
    return redirect('my-expenses')


def expense_category_summary(request):
    today = datetime.date.today()
    six_months_ago = today - datetime.timedelta(days=30 * 6)
    expenses = Expense.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=today)
    finalrep = {}

    def get_category(expense):
        return expense.category

    def get_expense_category_amount(category):
        amount = 0
        filtered_by_category = expenses.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    category_list = list(set(map(get_category, expenses)))

    for x in expenses:
        for y in category_list:
            finalrep[y] = get_expense_category_amount(y)
    return JsonResponse({'expense_category_data': finalrep}, safe=False)


def stats_view(request):
    return render(request, 'expenses/stats.html')


class AmountValidationView(View):

    def post(self, request):
        data = json.loads(request.body)
        amount = data['amount']

        if not re.match(r'^\d+(\.\d{1,2})?$', amount):
            return JsonResponse({'amount_error': 'please enter a positive whole Canadian dollar amount with a maximum '
                                                 'of 2 digits'}, status=400)
        return JsonResponse({'amount_valid': True})

        # if float(amount) > 1000.0:
        #     return JsonResponse({'amount_info': 'Please confirm the amount over $1000'}, status=200)
        # return JsonResponse({'amount_valid': True})


