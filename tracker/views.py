from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpResponseNotFound
from django.db import connection
from django.contrib import messages
from datetime import datetime
from .models import Category, Transaction, Transactions_by_Day, Monthly_Split, Yearly_Split, Monthly_Totals
from .forms import TransactionForm, DateForm
from .charts import generate_category_colours

# Create your views here.
def home(request):
    return render(
        request,
        "tracker/home.html"
    )

def get_transactions_by_day(request, month, year):
    #could probobly do this more elegantly looping through all categories and feeding them in
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
    daily_unassigned = get_transactions_by_day_by_category(request, month=month, year=year, category="Unassigned")

    colours = generate_category_colours()
    days = get_month_days(request, month=month, year=year)
    
    #https://testdriven.io/blog/django-charts/
    return JsonResponse({
        "data": {
            "labels": days,
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


def get_monthly_split(request, year, month):
    results = Monthly_Split.objects.raw(
        """
        SELECT 1 AS id, tot.cat_name, tot.monthly_total
                ,CAST(tot.monthly_total * 100 
                    / SUM(CASE WHEN monthly_total = 0 THEN 1 ELSE monthly_total END) OVER(PARTITION BY tot.username) AS DECIMAL(19,2)
                    ) AS pct
        FROM (
            SELECT 	cat.name AS cat_name
                    ,%s AS username
                    ,SUM(CASE WHEN amount IS NULL THEN 0 ELSE amount END) AS monthly_total
            FROM tracker_category cat
            LEFT JOIN (
                SELECT * 
                FROM tracker_transaction trn
                JOIN auth_user us ON trn.user_id = us.id
                WHERE transaction_date BETWEEN make_date(%s, %s, 1) 
                AND make_date(%s, %s, 1) + interval '1 month' - interval '1 day'
                AND us.username = %s
            ) trn ON cat.id = trn.category_id
            GROUP BY cat.name
        ) tot
        ORDER BY cat_name
        """
        ,[request.user.username, year, month, year, month, request.user.username]
    )

    colours = generate_category_colours()
    
    return JsonResponse({
        "data": {
            "labels": [res.cat_name for res in results],
            "datasets": [
            {
                "label": 'dataset 1',
                "data": [res.monthly_total for res in results],
                "backgroundColor": [colours[colour] for colour in colours],
            },]
        }}
    )


def get_month_days(request, month, year):
    results = Transactions_by_Day.objects.raw(
        """
        SELECT 1 as id, t.dt::date AS monthday
        FROM generate_series(
            make_date(%s, %s, 1)
            ,make_date(%s, %s, 1) + interval '1 month' - interval '1 day'
            ,interval '1 day'
        ) AS t(dt)
        """
        ,[year, month, year, month]
    )
    days = [res.monthday for res in results]
    return days


def get_current_dashboard(request):
    current_year = datetime.now().year
    current_month = datetime.now().month
    
    return HttpResponseRedirect(reverse('get_dashboard', args=[current_year, current_month]))


def route_to_chosen_dashboard(request):
    if request.method == "POST":
        date_form = DateForm(data=request.POST)
        if date_form.is_valid():
            year = request.POST.get("year")
            month = request.POST.get("month")
            return HttpResponseRedirect(reverse('get_month_dashboard', args=[year, month]))
    else:
        return HttpResponseNotFound("Page not found")


def get_month_dashboard(request, year, month):
    transactions = Transaction.objects.filter(
        user=request.user, transaction_date__year=year, transaction_date__month=month
        ).order_by("transaction_date")

    get_monthly_split(request=request, year=year, month=month)

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

    years = [yr for yr in range(2023, datetime.now().year + 1)]

    return render(
        request,
        "tracker/dashboard-month.html",
        {
            "transactions": transactions.order_by("transaction_date"),
            "years": years,
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

def get_year_dashboard(request, year):
    years = [yr for yr in range(2023, datetime.now().year + 1)]

    return render(
        request,
        "tracker/dashboard-year.html",
        {
            "years": years,
        }
    )


def get_yearly_split(request, year):
    results = Yearly_Split.objects.raw(
        """
        SELECT 1 AS id, cat_name, SUM(total_expenditure) AS yearly_total
        FROM daily_transactions trn
        WHERE username = %s AND yr = %s
        GROUP BY cat_name
        ORDER BY cat_name
        """
        ,[request.user.username, year]
    )

    colours = generate_category_colours()

    return JsonResponse({
        "data": {
            "labels": [res.cat_name for res in results],
            "datasets": [
            {
                "label": 'dataset 1',
                "data": [res.yearly_total for res in results],
                "backgroundColor": [colours[colour] for colour in colours],
            },]
        }}
    )


def get_year_by_month(request, year):
    results = Monthly_Totals.objects.raw(
        """
        SELECT 1 AS id, mnth AS month, SUM(total_expenditure) AS total_expenditure
        FROM daily_transactions trn
        WHERE username = %s AND yr = %s
        GROUP BY mnth
        ORDER BY mnth
        """
        ,[request.user.username, year]
    )
    
    return JsonResponse({
        "labels": [res.month for res in results],
        "datasets": [
            {
                "label": 'Dataset 1',
                "data": [res.total_expenditure for res in results],
                "borderColor": "#fc0303",
                "backgroundColor": "#fc0303",
            },
        ]
    })
    
   

