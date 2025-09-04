from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from .models import Campaign
from .forms import CampaignForm 
from django.views.generic import DetailView
# Create your views here.
@login_required
def dashboard(request):
    campaigns = Campaign.objects.filter(creator=request.user)
    return render(request, 'campaigns/dashboard.html', {'campaigns': campaigns})

@login_required
def create_campaign(request):
    if request.method == 'POST':
        form = CampaignForm(request.POST, request.FILES)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.creator = request.user
            campaign.save()
            return redirect('dashboard')
    else:
        form = CampaignForm()
    return render(request, 'campaigns/create_campaign.html', {'form': form})

class CampaignDetailView(DetailView):
    model = Campaign
    template_name = 'campaigns/detail.html'
    context_object_name = 'campaign'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress'] = (self.object.current_amount / self.object.target_amount) * 100
        return context
     
def donate(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    if request.method == 'POST':
        amount = request.POST.get('amount')
        # Here you would handle the donation logic, e.g., saving to a Donation model
        # For now, we just redirect to the campaign detail page
        return redirect('campaign_detail', pk=pk)
    return render(request, 'campaigns/donate.html', {'campaign': campaign})