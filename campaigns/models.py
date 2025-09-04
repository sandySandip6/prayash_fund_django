# campaigns/models.py
from django.db import models
from users.models import CustomUser

class Campaign(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    PROJECT_CATEGORY = [
        ('medical', 'Medical'),
        ('nature', 'Natural Clamities'),
        ('animal', 'Animal'),
        ('rites', 'Rites of Passage'),
        ('other', 'Other'),
    ]
    
    PAYMENT_METHOD = [
        ('esewa', 'E-Sewa'),
        ('khalti', 'Khalti'),
        ('mo_banking', 'Mobile Banking'),
        ('connect_ips', 'connectIPS'),
        ('bank_transfer', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]
    
    ACCOUNT_TYPE =[
        ('individual', 'Individual'),
        ('organization', 'Organization'),
        ('other', 'Other')
        
    ]
    
    PROJECT_FOR =[
        ('individual', 'Individual'),
        ('organization', 'Organization'),
        ('other', 'Other'),
    ]
    
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    project_for = models.CharField(default=False, choices=PROJECT_FOR)  # Optional field for project type
    account_type = models.CharField(default=False, choices=ACCOUNT_TYPE)  # Optional field for account type
    project_category = models.CharField(max_length=50, choices=PROJECT_CATEGORY, default=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255, blank=False, null=True) 
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, default=False)  # Optional field for payment method
    image = models.ImageField(upload_to='campaign_images/')
    
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/default_image.png'  # Default image if none is set 

    def __str__(self):
        return self.title