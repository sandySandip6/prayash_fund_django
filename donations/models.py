# donations/models.py
from django.db import models
from campaigns.models import Campaign
from users.models import CustomUser

class Donation(models.Model):
    PAYMENT_CHOICES = [
        ('esewa', 'Esewa'),
        ('khalti', 'Khalti'),
        ('mobile_banking', 'Mobile Banking'),
        ('connect_ips', 'Connect IPS'),
    ]
    
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    message = models.TextField(blank=True)
    donation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} donation to {self.campaign.title}"