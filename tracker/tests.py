from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .models import Transaction, Category
from .forms import TransactionForm

class TestViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.category = Category(name="Test Cat", description="Test Cat Desc")
        self.category.save()
        self.transaction = Transaction(amount=10.01, reference = "reference",user=self.user,
                         category=self.category, transaction_date="2024-01-01",
                         )
        self.transaction.save()

    def test_render_dashboard_month_page_with_transaction_form(self):
        self.client.login(
            username="myUsername", password="myPassword")
        response = self.client.get(reverse('get_month_dashboard',
                                            args=[2024,1]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Test Cat", response.content)
        self.assertIn(b"reference", response.content)
        self.assertIsInstance(
            response.context['transaction_form'], TransactionForm)

    def test_successful_transaction_adding(self):
        """Test for adding a transaction to the monthly dashboard page"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'amount': [0.01],
            'reference': ['demo - Unassigned'],
            'category': ['Test Cat'],
            'transaction_date': ['2024-07-10']
        }
        response = self.client.post(reverse(
            'get_month_dashboard', args=[2024,1]), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Transaction Added Successfully',
            response.content
        )

    def test_unsuccessful_transaction_adding(self):
        """Test for adding a transaction with no date"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'amount': [0.01],
            'reference': ['demo - Unassigned'],
            'category': ['Test Cat'],
            'transaction_date': ['']
        }
        response = self.client.post(reverse(
            'get_month_dashboard', args=[2024,1]), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(
            b'Transaction Added Successfully',
            response.content
        )