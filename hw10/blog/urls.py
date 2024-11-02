from django.urls import path
from . import views


urlpatterns=[
    #fill contents
    path('', views.index1, name='index1'),
    path('<int:pk>/', views.single_post_page),
]