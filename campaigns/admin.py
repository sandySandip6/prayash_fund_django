from django.contrib import admin
from .models import Campaign

# Register your models here.

class CampaignAdmin(admin.ModelAdmin):
    
    model = Campaign
    fields = ('title', 'description','status', 'target_amount', 'current_amount', 'image', 'creator')
    list_display = ('title', 'creator', 'target_amount', 'current_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'creator__username')
    readonly_fields = ('created_at', 'current_amount')
    ordering = ('-created_at',) 
    
admin.site.register(Campaign, CampaignAdmin) 
    
