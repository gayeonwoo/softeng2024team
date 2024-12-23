from django.urls import path
from . import views

urlpatterns = [
    path('', views.schedule_list, name='schedule_list'),
    path('add/', views.add_schedule, name='add_schedule'),
    path('edit/<int:id>/', views.edit_schedule, name='edit_schedule'),
    path('delete/<int:id>/', views.delete_schedule, name='delete_schedule'),
]
