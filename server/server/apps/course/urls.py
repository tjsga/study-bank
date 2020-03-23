from django.urls import path

from . import views

app_name = "course"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:course_url>", views.show, name="show"),
    path("<str:course_url>/approve/<int:doc_id>", views.approve, name="approve"),
    path("<str:course_url>/remove/<int:doc_id>", views.remove, name="remove"),
    path("<str:course_url>/undelete/<int:doc_id>", views.undelete, name="undelete"),
]