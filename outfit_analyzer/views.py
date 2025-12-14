import time
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OutfitUploadForm
from .models import OutfitAnalysis
from .services.ai_analyzer import OutfitAIAnalyzer


def home(request):
    """
    Home page with upload form
    """
    form = OutfitUploadForm()
    return render(request, 'outfit_analyzer/home.html', {'form': form})


def analyze_outfit(request):
    """
    Handle outfit upload and trigger AI analysis
    """
    if request.method == 'POST':
        form = OutfitUploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            # Save the upload
            analysis = form.save(commit=False)
            analysis.save()
            
            # Perform AI analysis
            start_time = time.time()
            
            try:
                analyzer = OutfitAIAnalyzer()
                result = analyzer.analyze_outfit(
                    image_path=analysis.image.path,
                    occasion=analysis.occasion,
                    gender=analysis.gender,
                    age=analysis.age
                )
                
                # Update analysis with results
                analysis.rating = result['rating']
                analysis.suggestions = result['suggestions']
                analysis.analysis_details = result.get('details', {})
                analysis.processing_time = time.time() - start_time
                analysis.save()
                
                messages.success(request, 'Your outfit has been analyzed!')
                return redirect('outfit_analyzer:result', analysis_id=analysis.id)
                
            except Exception as e:
                messages.error(request, f'Error analyzing outfit: {str(e)}')
                analysis.delete()  # Clean up if analysis fails
                return redirect('outfit_analyzer:home')
        
        else:
            messages.error(request, 'Please correct the errors below.')
            return render(request, 'outfit_analyzer/home.html', {'form': form})
    
    return redirect('outfit_analyzer:home')


def result(request, analysis_id):
    """
    Display analysis results
    """
    analysis = get_object_or_404(OutfitAnalysis, id=analysis_id)
    return render(request, 'outfit_analyzer/result.html', {'analysis': analysis})
