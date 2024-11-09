#표지판 파일

from django.urls import path,include
from . import views

app_name = 'single_pages'

urlpatterns = [
    path('gypage/', views.gypage, name='gypage'),
    path('kmpage/', views.kmpage, name='kmpage'),
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
]