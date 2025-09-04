# donations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('campaign/<int:pk>/', views.campaign_detail, name='campaign_detail'),
    path('donate/<int:pk>/', views.donate, name='donate'),
]