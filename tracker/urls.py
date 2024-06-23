from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path('dashboard/transaction_edit/<int:transaction_id>',
         views.transaction_edit, name='transaction_edit'),
]