from django.urls import path
from . import views

urlpatterns = [
    path("transactions/", views.home_form)
]