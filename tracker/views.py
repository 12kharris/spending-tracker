from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db import connection
from .models import Category, Transaction

# Create your views here.
def home(request):
    transactions = Transaction.objects.all().order_by("transaction_date")

    return render(
        request,
        "tracker/dashboard.html",
        {
            "transactions": transactions
        }
    )