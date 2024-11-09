from django.urls import path
from . import views

app_name = 'single_pages'

urlpatterns = [
    path("kmpage/", views.km, name="km"),
    path("", views.landing_page, name="landing"),
    path("gyPage/", views.gy, name="gy"),
    path("blog/", views.blog, name="blog"),
    path("todo/", views.todo, name="todo"),
]
