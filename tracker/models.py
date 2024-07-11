from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"


class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    reference = models.CharField(max_length=30, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="tracker_transaction"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT ,related_name = "tracker_transaction"
    )
    transaction_date = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-transaction_date"]

    def __str__(self):
        return f"{self.user.username} - {self.amount} | {self.reference} | {self.category} | {self.transaction_date}"


class Daily_Transactions(models.Model):
    unique_id   = models.CharField(max_length=255, primary_key=True)
    day_of_year = models.DateField()
    mnth = models.IntegerField()
    username = models.CharField(max_length=150, blank=False)
    cat_name = models.CharField()
    total_expenditure = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        managed = False,
        db_table = "Daily_Transactions"


class Transactions_by_Day(models.Model):
    day_of_year = models.DateField()
    mnth = models.IntegerField()
    yr = models.IntegerField()
    username = models.CharField(max_length=150, blank=False)
    cat_name = models.CharField()
    total_expenditure = models.DecimalField(decimal_places=2, max_digits=10)

    # class Meta:
    #     managed = False


class Monthly_Split(models.Model):
    cat_name = models.CharField()
    monthly_total = models.DecimalField(decimal_places=2, max_digits=10)
    pct = models.DecimalField(decimal_places=2, max_digits=5)

    # class Meta:
    #     managed = False


class Yearly_Split(models.Model):
    cat_name = models.CharField()
    yearly_total = models.DecimalField(decimal_places=2, max_digits=10)

    # class Meta:
    #     managed = False


class Monthly_Totals(models.Model):
    month = models.IntegerField()
    total_expenditure = models.DecimalField(decimal_places=2, max_digits=10)

    # class Meta:
    #     managed = False