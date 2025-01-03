from django.urls import path
from mypy.types import names

from . import views

app_name = 'blog'

urlpatterns=[
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),
    path('create_post/',views.PostCreate.as_view()),
    path('tag/<str:slug>/', views.tag_page),
    path('category/<str:slug>/', views.category_page),
    path('', views.PostList.as_view(), name='notice'),
    path('<int:pk>/', views.PostDetail.as_view()),
]