from django import forms
from .models import OutfitAnalysis


class OutfitUploadForm(forms.ModelForm):
    """
    Form for uploading outfit images and providing context
    """
    
    class Meta:
        model = OutfitAnalysis
        fields = ['image', 'occasion', 'gender', 'age']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
            'occasion': forms.Select(attrs={
                'class': 'form-select',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select',
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '13',
                'max': '100',
                'placeholder': 'Enter your age',
            }),
        }
        labels = {
            'image': 'Upload Your Outfit Photo',
            'occasion': 'Select Occasion',
            'gender': 'Gender',
            'age': 'Age',
        }
    
    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Validate file size (max 10MB)
            if image.size > 10 * 1024 * 1024:
                raise forms.ValidationError('Image file too large ( > 10MB )')
            
            # Validate file type
            valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
            ext = image.name.split('.')[-1].lower()
            if ext not in valid_extensions:
                raise forms.ValidationError('Only JPG, PNG, and WebP images are allowed.')
        
        return image
