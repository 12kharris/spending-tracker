from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.description}"


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