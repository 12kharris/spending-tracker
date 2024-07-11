from .models import Transaction, Category
from django import forms

#https://stackoverflow.com/questions/31548373/django-1-8-django-crispy-forms-is-there-a-simple-easy-way-of-implementing-a
class TransactionForm(forms.Form):
    amount = forms.DecimalField(max_digits=10,decimal_places=2)
    reference = forms.CharField(max_length=30)
    category = forms.ModelChoiceField(queryset=Category.objects.all().exclude(name='Unassigned'))
    transaction_date = forms.DateField(
        widget=forms.TextInput(     
            attrs={'type': 'date'} 
        )
    )             

class DateForm(forms.Form):
    year = forms.IntegerField()
    month = forms.CharField()


class YearForm(forms.Form):
    year = forms.IntegerField()