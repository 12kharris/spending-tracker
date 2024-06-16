from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.db import connection
from .models import Category, Transaction

# Create your views here.
def home(request):
    return HttpResponse("home")


def dashboard(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("transaction_date")

    return render(
        request,
        "tracker/dashboard.html",
        {
            "transactions": transactions
        }
    )