from django.urls import path
from . import views

app_name = 'outfit_analyzer'

urlpatterns = [
    path('', views.home, name='home'),
    path('analyze/', views.analyze_outfit, name='analyze'),
    path('result/<int:analysis_id>/', views.result, name='result'),
]
