from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voters/', views.voter_search, name='voters')
]