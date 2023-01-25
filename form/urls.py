from django.urls import path
from .views import UploadView

urlpatterns = [
    path("form/", UploadView.as_view()),
]