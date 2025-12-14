from django.contrib import admin
from .models import OutfitAnalysis


@admin.register(OutfitAnalysis)
class OutfitAnalysisAdmin(admin.ModelAdmin):
    list_display = ['id', 'occasion', 'gender', 'age', 'rating', 'created_at']
    list_filter = ['occasion', 'gender', 'created_at']
    search_fields = ['suggestions']
    readonly_fields = ['created_at', 'processing_time']
    
    fieldsets = (
        ('User Input', {
            'fields': ('image', 'occasion', 'gender', 'age')
        }),
        ('AI Analysis', {
            'fields': ('rating', 'suggestions', 'analysis_details')
        }),
        ('Metadata', {
            'fields': ('created_at', 'processing_time')
        }),
    )
