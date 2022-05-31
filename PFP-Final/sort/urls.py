from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sort1/', views.sort1, name='sort1'),
    path('sort2/', views.sort2, name='sort2'),
    path('sort3/', views.sort3, name='sort3')
]
