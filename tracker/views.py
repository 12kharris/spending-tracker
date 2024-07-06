from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.db import connection
from django.contrib import messages
from .models import Category, Transaction, Transactions_by_Day
from .forms import TransactionForm
from .charts import generate_category_colours

# Create your views here.
def home(request):
    return render(
        request,
        "tracker/home.html"
    )

def get_transactions_by_day(request, month, year):
    #here do queries for each category and return them to feed into the data sets
    #could probobly do this more elgantly looping through all categories and feeding them in
    daily_housing = get_transactions_by_day_by_category(request, month=month, year=year, category="Housing")
    daily_car = get_transactions_by_day_by_category(request, month=month, year=year, category="Car")
    daily_groceries = get_transactions_by_day_by_category(request, month=month, year=year, category="Groceries")
    daily_dining_out = get_transactions_by_day_by_category(request, month=month, year=year, category="Dining Out")
    daily_subscriptions = get_transactions_by_day_by_category(request, month=month, year=year, category="Subscriptions")
    daily_clothes = get_transactions_by_day_by_category(request, month=month, year=year, category="Clothes")
    daily_leisure = get_transactions_by_day_by_category(request, month=month, year=year, category="Leisure")
    daily_education = get_transactions_by_day_by_category(request, month=month, year=year, category="Education")
    daily_presents = get_transactions_by_day_by_category(request, month=month, year=year, category="Presents")
    daily_miscellaneous = get_transactions_by_day_by_category(request, month=month, year=year, category="Miscellaneous")
    daily_unassigned = get_transactions_by_day_by_category(request, month=month, year=year, category="Unassgined")

    colours = generate_category_colours()
    
    #https://testdriven.io/blog/django-charts/
    return JsonResponse({
        "data": {
            "labels": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10","11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30" ],
            "datasets": [
            {
                "label": 'Housing',
                "data": daily_housing,
                "backgroundColor": colours["Housing"],
            },
            {
                "label": 'Car',
                "data": daily_car,
                "backgroundColor": colours["Car"],
            },
            {
                "label": 'Groceries',
                "data": daily_groceries,
                "backgroundColor": colours["Groceries"],
            },
            {
                "label": 'Dining Out',
                "data": daily_dining_out,
                "backgroundColor": colours["Dining Out"],
            },
            {
                "label": 'Subscriptions',
                "data": daily_subscriptions,
                "backgroundColor": colours["Subscriptions"],
            },
            {
                "label": 'Clothing',
                "data": daily_clothes,
                "backgroundColor": colours["Clothes"],
            },
            {
                "label": 'Leisure',
                "data": daily_leisure,
                "backgroundColor": colours["Leisure"],
            },
            {
                "label": 'Education',
                "data": daily_education,
                "backgroundColor": colours["Education"],
            },
            {
                "label": 'Presents',
                "data": daily_presents,
                "backgroundColor": colours["Presents"],
            },
            {
                "label": 'Miscellaneous',
                "data": daily_miscellaneous,
                "backgroundColor": colours["Miscellaneous"],
            },
            {
                "label": 'Unassigned',
                "data": daily_unassigned,
                "backgroundColor": colours["Unassigned"],
            },
            ]
        }
    })


def get_transactions_by_day_by_category(request, month, year, category):
    results = Transactions_by_Day.objects.raw(
        """
        SELECT 1 AS id, * 
        FROM Daily_Transactions 
        WHERE username = %s AND mnth = %s AND yr = %s AND cat_name = %s
        ORDER BY day_of_year, cat_name
        """
        ,[request.user.username, month, year, category]
    )
    
    daily_res = [res.total_expenditure for res in results]
    return daily_res


def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("transaction_date")

    if request.method == "POST":
        transaction_form = TransactionForm(data=request.POST)
        if(transaction_form.is_valid()):
            #https://stackoverflow.com/questions/16443029/cant-save-a-form-in-django-object-has-no-attribute-save
            cd = transaction_form.cleaned_data
            transaction = Transaction(
                amount = cd['amount'], 
                reference= cd['reference'],
                user = request.user,
                category = cd['category'],
                transaction_date = cd['transaction_date']
            )
            transaction.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Transaction Added Successfully'
            )

    transaction_form = TransactionForm()

    return render(
        request,
        "tracker/dashboard.html",
        {
            "transactions": transactions.order_by("transaction_date"),
            #"transactions_by_day": transactions_by_day,
            "transaction_form": transaction_form
        }
    )


def transaction_edit(request, transaction_id):
    if request.method == "POST":
        queryset = Transaction.objects.filter(user=request.user, id=transaction_id)
        transaction = get_object_or_404(queryset, id=transaction_id)
        transaction_form = TransactionForm(data=request.POST)

        if transaction_form.is_valid() and transaction.user == request.user:
            cd = transaction_form.cleaned_data
            transaction.amount = cd['amount']
            transaction.reference = cd['reference']
            transaction.category = cd['category']
            transaction.transaction_date = cd['transaction_date']
            transaction.save()
            messages.add_message(request, messages.SUCCESS, 'Transaction Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating transaction!')

    return HttpResponseRedirect(reverse('dashboard'))


def transaction_delete(request, transaction_id):
    transaction = get_object_or_404(Transaction.objects.filter(user=request.user, id = transaction_id), id = transaction_id)

    if transaction.user == request.user:
        transaction.delete()
        messages.add_message(request, messages.SUCCESS, "Transaction deleted") #could add details of the deleted transaction
    else:
        messages.add_message(request, messages.ERROR, "Error deleting transaction")

    return HttpResponseRedirect(reverse('dashboard'))
