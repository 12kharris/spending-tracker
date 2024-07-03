from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/<int:year>/<int:month>", views.get_transactions_by_day, name="get_transactions_by_day"),
    path('dashboard/transaction_edit/<int:transaction_id>',
         views.transaction_edit, name='transaction_edit'),
    path('dashboard/transaction_delete/<int:transaction_id>',
         views.transaction_delete, name='transaction_delete'),
]