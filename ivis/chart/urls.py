from django.urls import path

from . import views

app_name = "chart"

urlpatterns = [
    path("", views.index, name="chart_index"),
]
