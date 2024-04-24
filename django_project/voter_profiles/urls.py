from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voters/', views.voter_search, name='voters'),
    path('voters/<str:id>/', views.voter_detail, name='voter_detail')
]