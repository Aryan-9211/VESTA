"""
AI Analyzer Service for Outfit Rating
Uses OpenAI GPT-4 Vision API to analyze outfits
"""

import base64
import os
from typing import Dict, Any
from openai import OpenAI
from django.conf import settings


class OutfitAIAnalyzer:
    """
    Service class to handle AI-powered outfit analysis
    """
    
    def __init__(self):
        """Initialize OpenAI client"""
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    def _encode_image(self, image_path: str) -> str:
        """Encode image to base64 string"""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
    
    def _build_prompt(self, occasion: str, gender: str, age: int) -> str:
        """
        Build the prompt for AI analysis
        """
        prompt = f"""You are a professional fashion consultant. Analyze this outfit image and provide:

1. A rating from 1 to 10 (where 10 is perfect for the occasion)
2. Detailed improvement suggestions

Context:
- Occasion: {occasion}
- Gender: {gender}
- Age: {age}

Consider:
- Color coordination and contrast
- Fit and proportion
- Appropriateness for the occasion
- Style and current fashion trends
- Accessories and overall presentation

Provide your response in the following JSON format:
{{
    "rating": <number between 1-10>,
    "overall_impression": "<brief overall assessment>",
    "strengths": ["<strength 1>", "<strength 2>", ...],
    "improvements": ["<improvement 1>", "<improvement 2>", ...],
    "specific_suggestions": {{
        "colors": "<color suggestions>",
        "fit": "<fit suggestions>",
        "styling": "<styling suggestions>",
        "accessories": "<accessory suggestions>"
    }}
}}

Be constructive, specific, and helpful in your feedback."""
        return prompt
    
    def analyze_outfit(
        self, 
        image_path: str, 
        occasion: str, 
        gender: str, 
        age: int
    ) -> Dict[str, Any]:
        """
        Analyze outfit using OpenAI Vision API
        
        Args:
            image_path: Path to the outfit image
            occasion: The occasion (office, date, college, etc.)
            gender: Gender context
            age: Age of the person
        
        Returns:
            Dictionary with rating and suggestions
        """
        
        # Encode image
        base64_image = self._encode_image(image_path)
        
        # Build prompt
        prompt = self._build_prompt(occasion, gender, age)
        
        # Call OpenAI API
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",  # Using GPT-4 Omni (vision model)
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": prompt
                            },
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1000,
                temperature=0.7,
            )
            
            # Parse response
            content = response.choices[0].message.content
            
            # Extract JSON from response
            import json
            # Try to find JSON in the response
            if '```json' in content:
                json_str = content.split('```json')[1].split('```')[0].strip()
            elif '```' in content:
                json_str = content.split('```')[1].split('```')[0].strip()
            else:
                json_str = content.strip()
            
            result = json.loads(json_str)
            
            # Format suggestions for display
            suggestions_text = self._format_suggestions(result)
            
            return {
                'rating': float(result['rating']),
                'suggestions': suggestions_text,
                'details': result
            }
            
        except Exception as e:
            raise Exception(f"AI Analysis failed: {str(e)}")
    
    def _format_suggestions(self, analysis: Dict[str, Any]) -> str:
        """
        Format the AI analysis into readable suggestions text
        """
        parts = []
        
        # Overall impression
        if 'overall_impression' in analysis:
            parts.append(f"**Overall:** {analysis['overall_impression']}\n")
        
        # Strengths
        if 'strengths' in analysis and analysis['strengths']:
            parts.append("**What's Working Well:**")
            for strength in analysis['strengths']:
                parts.append(f"• {strength}")
            parts.append("")
        
        # Improvements
        if 'improvements' in analysis and analysis['improvements']:
            parts.append("**Areas for Improvement:**")
            for improvement in analysis['improvements']:
                parts.append(f"• {improvement}")
            parts.append("")
        
        # Specific suggestions
        if 'specific_suggestions' in analysis:
            parts.append("**Specific Recommendations:**")
            suggestions = analysis['specific_suggestions']
            
            if suggestions.get('colors'):
                parts.append(f"🎨 **Colors:** {suggestions['colors']}")
            
            if suggestions.get('fit'):
                parts.append(f"👔 **Fit:** {suggestions['fit']}")
            
            if suggestions.get('styling'):
                parts.append(f"✨ **Styling:** {suggestions['styling']}")
            
            if suggestions.get('accessories'):
                parts.append(f"💍 **Accessories:** {suggestions['accessories']}")
        
        return "\n".join(parts)
