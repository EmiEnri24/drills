from django.urls import path
from expenses.api import views

urlpatterns = [
    path("expenses/",views.expenses_list),
    path("expenses/<int:pk>/",views.expense_detail),
]