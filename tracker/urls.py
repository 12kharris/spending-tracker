from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.get_current_dashboard, name="dashboard"),
    path("dashboard/get", views.route_to_chosen_dashboard, name="route_to_dashboard"),
    path("dashboard/<int:year>/<int:month>/", views.get_dashboard, name="get_dashboard"),
    path("dashboard/<int:year>/<int:month>/raw", views.get_transactions_by_day, name="get_transactions_by_day"),
    path("dashboard/<int:year>/<int:month>/split", views.get_monthly_split, name="get_monthly_split"),
    path('dashboard/transaction_edit/<int:transaction_id>',views.transaction_edit, name='transaction_edit'),
    path('dashboard/transaction_delete/<int:transaction_id>',views.transaction_delete, name='transaction_delete'),
]