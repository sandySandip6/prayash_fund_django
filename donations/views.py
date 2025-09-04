# donations/views.py
from django.shortcuts import render, redirect, get_object_or_404
from campaigns.models import Campaign
from .forms import DonationForm
from django.contrib import messages

def campaign_detail(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    return render(request, 'donations/detail.html', {'campaign': campaign})

def donate(request, pk):
    campaign = get_object_or_404(Campaign, pk=pk)
    
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.campaign = campaign
            
            # Update campaign amount
            campaign.current_amount += donation.amount
            campaign.save()
            
            donation.save()
            messages.success(request, 'Thank you for your donation!')
            return redirect('index')
    else:
        form = DonationForm()

    return render(request, 'donations/donate.html', {
        'form': form,
        'campaign': campaign
    })