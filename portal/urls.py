from django.urls import path
from . import views

app_name = "portal"

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("patients/", views.patients_list, name="patients"),
    path("patients/new/", views.patients_create, name="patients_create"),
    path("settings/", views.settings_view, name="settings"),
    path("about/", views.about, name="about"),
]
