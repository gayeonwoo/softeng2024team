from django.urls import path
from .views import keypad_input
from . import views

app_name = 'management'

urlpatterns=[
    path('', views.weather_warning, name='management'),
    path('edit/', views.PostUpdate.as_view(), name='edit'),
path('api/keypad_input/', keypad_input, name='keypad_input'),
    ]