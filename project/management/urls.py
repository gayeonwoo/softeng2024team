from django.urls import path

from . import views

app_name = 'management'

urlpatterns=[
    path('', views.weather_warning, name='management'),
    path('edit/', views.PostUpdate.as_view(), name='edit'),
    ]