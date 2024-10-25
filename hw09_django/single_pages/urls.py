from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path("kmpage/", views.km, name="km"),
    path("", views.landing_page, name="landing"),
    path("gyPage/", views.gy, name="gy")
]
