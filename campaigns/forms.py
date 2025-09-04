# campaigns/forms.py
from django import forms
from .models import Campaign

class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        fields = ['project_for','account_type','project_category','title', 'description','address','target_amount', 'payment_method','image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }