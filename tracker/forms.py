from .models import Transaction, Category
from django import forms

class TransactionForm(forms.Form):
    amount = forms.DecimalField(max_digits=10,decimal_places=2)
    reference = forms.CharField(max_length=30)
    category = forms.ModelChoiceField(queryset=Category.objects.all().exclude(name='Unassigned'))
    transaction_date = forms.DateField()