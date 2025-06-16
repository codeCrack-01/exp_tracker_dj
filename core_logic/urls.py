from django.urls import path

from core_logic.views import HomePageView, CreateEntryView, UpdateEntryView, DeleteEntryView
from core_logic.views import redirect_main

urlpatterns = [
    path("", redirect_main, name="temp"),
    path("expense", HomePageView.as_view(), name='home'),
    path("expense/add_expense", CreateEntryView.as_view() ,name='add_entry'),
    path("expense/<int:pk>/update/", UpdateEntryView.as_view(), name='update_entry'),
    path("expense/<int:pk>/delete/", DeleteEntryView.as_view(), name='delete_entry'),
]
