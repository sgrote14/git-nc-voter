from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('voters/', views.voter_search, name='voters'),
    path('voters/<str:ncid>/', views.voter_detail, name='voter_detail'),
    path('county/<int:county_id>/', views.county_view, name='county_view'),
    path('get_precincts/', views.get_precincts, name='get_precincts'),
    path('analytics/', views.analytics, name='analytics'),
    path('api/', views.api, name='api')
]
