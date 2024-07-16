from django.db import connection
from datetime import datetime, date
from .models import Category, Transaction, Monthly_Split, Transactions_by_Day
from .models import Yearly_Split, Monthly_Totals
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.http import HttpResponseNotFound
from .forms import TransactionForm, DateForm, YearForm
from .charts import generate_category_colours


# Create your views here.
def home(request):
    """
    Returns the template for the home page
    """
    return render(
        request,
        "tracker/home.html"
    )


def get_transactions_by_day(request, month, year):
    """
    Returns JSON data for monthly dashboard daily stacked bar chart generation
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    # could probobly do this more elegantly looping through all categories and
    # feeding them into a generic function
    daily_housing = get_transactions_by_day_by_category(request, month=month,
                                                        year=year,
                                                        category="Housing")
    daily_car = get_transactions_by_day_by_category(request, month=month,
                                                    year=year,
                                                    category="Car")
    daily_groceries = get_transactions_by_day_by_category(request, month=month,
                                                          year=year,
                                                          category="Groceries")
    daily_dining_out = get_transactions_by_day_by_category(request,
                                                           month=month,
                                                           year=year,
                                                           category="Dining"
                                                           + "Out"
                                                           )
    daily_subscriptions = get_transactions_by_day_by_category(request,
                                                              month=month,
                                                              year=year,
                                                              category="Sub"
                                                              + "scriptions")
    daily_clothes = get_transactions_by_day_by_category(request, month=month,
                                                        year=year,
                                                        category="Clothes")
    daily_leisure = get_transactions_by_day_by_category(request, month=month,
                                                        year=year,
                                                        category="Leisure")
    daily_education = get_transactions_by_day_by_category(request, month=month,
                                                          year=year,
                                                          category="Education")
    daily_presents = get_transactions_by_day_by_category(request, month=month,
                                                         year=year,
                                                         category="Presents")
    daily_miscellaneous = get_transactions_by_day_by_category(request,
                                                              month=month,
                                                              year=year,
                                                              category="Misc"
                                                              + "ellaneous")
    daily_unassigned = get_transactions_by_day_by_category(request,
                                                           month=month,
                                                           year=year,
                                                           category="Un"
                                                           + "assigned")

    colours = generate_category_colours()
    days = get_month_days(request, month=month, year=year)

    # https://testdriven.io/blog/django-charts/
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
    """
    Returns the daily expenditure in the given year and month for the specified
     category
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    results = Transactions_by_Day.objects.raw(
        """
        SELECT 1 AS id, *
        FROM Daily_Transactions
        WHERE username = %s AND mnth = %s AND yr = %s AND cat_name = %s
        ORDER BY day_of_year, cat_name
        """,
        [request.user.username, month, year, category]
    )

    daily_res = [res.total_expenditure for res in results]
    return daily_res


def get_monthly_split(request, year, month):
    """
    Returns JSON data for expenditure in each category for the given month.
    Used in the monthly pie chart generation
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    # get all categories and the total expenditure over the month for the
    # given user
    # also includes the % split
    results = Monthly_Split.objects.raw(
        """
        SELECT 1 AS id, tot.cat_name, tot.monthly_total
                ,CAST(tot.monthly_total * 100
                    / SUM(CASE WHEN monthly_total = 0 THEN 1
                        ELSE monthly_total END)
                        OVER(PARTITION BY tot.username) AS DECIMAL(19,2)
                    ) AS pct
        FROM (
            SELECT 	cat.name AS cat_name
                    ,%s AS username
                    ,SUM(CASE WHEN amount IS NULL THEN 0 ELSE amount END)
                        AS monthly_total
            FROM tracker_category cat
            LEFT JOIN (
                SELECT *
                FROM tracker_transaction trn
                JOIN auth_user us ON trn.user_id = us.id
                WHERE transaction_date BETWEEN make_date(%s, %s, 1)
                AND make_date(%s, %s, 1)
                    + interval '1 month' - interval '1 day'
                AND us.username = %s
            ) trn ON cat.id = trn.category_id
            GROUP BY cat.name
        ) tot
        ORDER BY cat_name
        """,
        [request.user.username, year, month, year, month,
         request.user.username]
    )

    colours = generate_category_colours()

    return JsonResponse({
        "data": {
            "labels": [res.cat_name for res in results],
            "datasets": [
                {
                    "label": 'Monthly Total',
                    "data": [res.monthly_total for res in results],
                    "backgroundColor": [colours[colour] for colour in colours],
                },
            ]
        }}
    )


def get_month_days(request, month, year):
    """
    Get a list of days in the given month.
    Used as labels on the daily stacked bar chart
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    results = Transactions_by_Day.objects.raw(
        """
        SELECT 1 as id, t.dt::date AS monthday
        FROM generate_series(
            make_date(%s, %s, 1)
            ,make_date(%s, %s, 1) + interval '1 month' - interval '1 day'
            ,interval '1 day'
        ) AS t(dt)
        """,
        [year, month, year, month]
    )
    days = [res.monthday for res in results]
    return days


def get_current_dashboard(request):
    """
    Navigate to the dashboard for the present month
    """
    current_year = datetime.now().year
    current_month = datetime.now().month

    return HttpResponseRedirect(reverse('get_month_dashboard',
                                args=[current_year, current_month]))


def route_to_chosen_dashboard(request):
    """
    Navigate to the dashboard of the specified month and/or year
    """
    if request.method == "POST":
        date_form = DateForm(data=request.POST)
        if date_form.is_valid():
            year = request.POST.get("year")
            month = request.POST.get("month")

            current_year = datetime.now().year
            current_month = datetime.now().month

            # logic to prevent access to future months/years
            if month == "All":
                if int(year) > current_year:
                    return HttpResponseRedirect(reverse('get_year_dashboard',
                                                args=[current_year]))
                return HttpResponseRedirect(reverse('get_year_dashboard',
                                            args=[year]))
            elif int(year) > current_year or (year == current_year
                                         and int(month) > int(current_month)):
                return HttpResponseRedirect(reverse('get_month_dashboard',
                                                    args=[current_year,
                                                          current_month]))
            else:
                return HttpResponseRedirect(reverse('get_month_dashboard',
                                             args=[year, month]))

    else:
        return HttpResponseNotFound("Page not found")


# REDUNDANT???
def route_to_chosen_year_dashboard(request):
    """

    """
    if request.method == "POST":
        year_form = YearForm(data=request.POST)
        if year_form.is_valid():
            year = request.POST.get("year")
            return HttpResponseRedirect(reverse('get_year_dashboard',
                                        args=[year]))
    else:
        return HttpResponseNotFound("Page not found")


def get_month_dashboard(request, year, month):
    """
    Generates and returns the monthly dashboard view.
    Handles adding of new transactions from 'add' form.
    Gets the transactions in the specified month and return them in the
    monthly dashboard view
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    transactions = Transaction.objects.filter(
        user=request.user,
        transaction_date__year=year,
        transaction_date__month=month
        ).order_by("transaction_date")

    # calc the total expenditure in the given month
    total_expenditure = 0
    for trn in transactions:
        total_expenditure += trn.amount

    # handle submission of 'add' form to create new transactions
    if request.method == "POST":
        # convert all submitted 'amounts' to 2 dp
        post = request.POST.copy()
        post["amount"] = round(float(request.POST.get("amount")), 2)
        request.POST = post

        transaction_form = TransactionForm(data=request.POST)

        if (transaction_form.is_valid()):
            # https://stackoverflow.com/questions/16443029/cant-save-a-form
            # -in-django-object-has-no-attribute-save
            cd = transaction_form.cleaned_data

            category = Category.objects.filter(name=cd['category'])

            transaction = Transaction(
                amount=cd['amount'],
                reference=cd['reference'],
                user=request.user,
                category=category[0],
                transaction_date=cd['transaction_date']
            )
            transaction.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Transaction Added Successfully'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Error adding transaction'
            )

    transaction_form = TransactionForm()

    # get all years for options in form for choosing date
    years = [yr for yr in range(2023, datetime.now().year + 1)]
    month_name = date(year, month, 1).strftime('%B')

    return render(
        request,
        "tracker/dashboard-month.html",
        {
            "transactions": transactions.order_by("transaction_date"),
            "total_exp": total_expenditure,
            "years": years,
            "transaction_form": transaction_form,
            "chosen_month_name": month_name,
            "chosen_year": year
        }
    )


def transaction_edit(request, year, month, transaction_id):
    """
    Handle editing of existing transactions
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    if request.method == "POST":
        # convert all submitted 'amounts' to 2 dp
        post = request.POST.copy()
        post["amount"] = round(float(request.POST.get("amount")), 2)
        request.POST = post

        queryset = Transaction.objects.filter(user=request.user,
                                              id=transaction_id)
        transaction = get_object_or_404(queryset, id=transaction_id)
        transaction_form = TransactionForm(data=request.POST)

        if transaction_form.is_valid() and transaction.user == request.user:
            cd = transaction_form.cleaned_data
            category = Category.objects.filter(name=cd['category'])

            transaction.amount = cd['amount']
            transaction.reference = cd['reference']
            transaction.category = category[0]
            transaction.transaction_date = cd['transaction_date']
            transaction.save()

            messages.add_message(request, messages.SUCCESS,
                                 'Transaction Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating transaction!')

    return HttpResponseRedirect(reverse('get_month_dashboard',
                                args=[year, month]))


def transaction_delete(request, year, month, transaction_id):
    """
    Handle deletion of existing transactions
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    transaction = get_object_or_404(Transaction.objects.filter(
        user=request.user, id=transaction_id), id=transaction_id)

    if transaction.user == request.user:
        transaction.delete()
        # could add details of the deleted transaction
        messages.add_message(request, messages.SUCCESS, "Transaction deleted")
    else:
        messages.add_message(request, messages.ERROR,
                             "Error deleting transaction")

    return HttpResponseRedirect(reverse('get_month_dashboard',
                                args=[year, month]))


def get_year_dashboard(request, year):
    """
    Return the yearly dashboard template and total yearly expenditure
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    transactions = Transaction.objects.filter(
        user=request.user, transaction_date__year=year
    )

    total_expenditure = 0
    for trn in transactions:
        total_expenditure += trn.amount

    # get all years for options in dashboard date form
    years = [yr for yr in range(2023, datetime.now().year + 1)]

    return render(
        request,
        "tracker/dashboard-year.html",
        {
            "years": years,
            "chosen_year": year,
            "total_exp": total_expenditure
        }
    )


def get_yearly_split(request, year):
    """
    Returns JSON data for expenditure in each category for the given year.
    Used in the yearly pie chart generation
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    results = Yearly_Split.objects.raw(
        """
        SELECT 1 AS id, cat_name, SUM(total_expenditure) AS yearly_total
        FROM daily_transactions trn
        WHERE username = %s AND yr = %s
        GROUP BY cat_name
        ORDER BY cat_name
        """,
        [request.user.username, year]
    )

    colours = generate_category_colours()

    return JsonResponse({
        "data": {
            "labels": [res.cat_name for res in results],
            "datasets": [
                {
                    "label": 'Yearly Total',
                    "data": [res.yearly_total for res in results],
                    "backgroundColor": [colours[colour] for colour in colours],
                },
            ]
        }}
    )


def get_year_by_month(request, year):
    """
    Generate JSON data for the total expenditure per month for the given year.
    Used in the monthly line chart generation
    """
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home"))

    results = Monthly_Totals.objects.raw(
        """
        SELECT 1 AS id, mnth AS month, SUM(total_expenditure)
            AS total_expenditure
        FROM daily_transactions trn
        WHERE username = %s AND yr = %s
        GROUP BY mnth
        ORDER BY mnth
        """,
        [request.user.username, year]
    )

    return JsonResponse({
        "data": {
            "labels": [res.month for res in results],
            "datasets": [
                {
                    "label": 'Total Expenditure',
                    "data": [res.total_expenditure for res in results],
                    "borderColor": "#fc0303",
                    "backgroundColor": "#fc0303",
                },
            ]
        }
    })
