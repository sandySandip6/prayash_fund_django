from django.shortcuts import render, redirect 
from campaigns.models import Campaign

def index(request):
    template_name = 'index.html'    
    campaign = Campaign.objects.filter(status='approved').order_by('-created_at')[:3]  # Get the latest 3 active campaigns
    context = {
        'campaigns': campaign,
    }
    return render(request, template_name, context)