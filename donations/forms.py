# donations/forms.py
from django import forms
from .models import Donation

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['payment_method', 'amount', 'message']
        widgets = {
            'payment_method': forms.RadioSelect(),
            'amount': forms.NumberInput(attrs={'min': 1}),
            'message': forms.Textarea(attrs={'rows': 3}),
        }
