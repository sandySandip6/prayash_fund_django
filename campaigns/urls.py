from django.urls import path
from . import views 

urlpatterns = [
    path('start-campaigns/', views.dashboard, name='dashboard'),
    path('create-campaign/', views.create_campaign, name='create_campaign'),
    path('campaign/<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('campaign/<int:pk>/donate/', views.donate, name='donate'),
]
