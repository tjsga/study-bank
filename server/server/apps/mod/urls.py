from django.urls import path

from . import views

app_name = "mod"

urlpatterns = [
    path("", views.dashboard, name="dash"),
]