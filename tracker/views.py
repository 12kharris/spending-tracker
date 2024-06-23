from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.db import connection
from django.contrib import messages
from .models import Category, Transaction
from .forms import TransactionForm

# Create your views here.
def home(request):
    return render(
        request,
        "tracker/home.html"
    )


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
            "transactions": transactions,
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