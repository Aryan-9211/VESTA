from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class OutfitAnalysis(models.Model):
    """
    Model to store outfit analysis results.
    Keeps history of all analyses for future features (analytics, history, etc.)
    """
    
    OCCASION_CHOICES = [
        ('office', 'Office'),
        ('date', 'Date'),
        ('college', 'College'),
        ('casual', 'Casual'),
        ('formal', 'Formal Event'),
        ('party', 'Party'),
    ]
    
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]
    
    # User inputs
    image = models.ImageField(upload_to='outfit_images/%Y/%m/%d/')
    occasion = models.CharField(max_length=20, choices=OCCASION_CHOICES)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.IntegerField(
        validators=[MinValueValidator(13), MaxValueValidator(100)]
    )
    
    # AI Analysis results
    rating = models.DecimalField(
        max_digits=3, 
        decimal_places=1,
        validators=[MinValueValidator(1.0), MaxValueValidator(10.0)],
        null=True,
        blank=True
    )
    suggestions = models.TextField(blank=True)
    analysis_details = models.JSONField(default=dict, blank=True)  # For structured data
    
    # Metadata
    created_at = models.DateTimeField(auto_now_add=True)
    processing_time = models.FloatField(null=True, blank=True)  # in seconds
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Outfit Analysis'
        verbose_name_plural = 'Outfit Analyses'
    
    def __str__(self):
        return f"{self.occasion} - {self.gender} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
