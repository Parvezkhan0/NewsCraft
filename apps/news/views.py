from django.shortcuts import render, get_object_or_404
from .models import Article
import requests
from django.conf import settings

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    # Use Hugging Face API instead of local model
    try:
        headers = {
            "Authorization": f"Bearer {settings.HUGGINGFACE_API_KEY}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "inputs": article.content[:1000],  # Limit content length
            "parameters": {
                "max_length": 150,
                "min_length": 50
            }
        }
        
        response = requests.post(
            "https://api-inference.huggingface.co/models/facebook/bart-large-cnn",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            summarized_text = result[0]['summary_text'] if result else "Summary not available"
        else:
            summarized_text = "Summary not available"
            
    except Exception as e:
        summarized_text = "Summary not available"
    
    return render(request, 'news/article_detail.html', {
        'article': article, 
        'summary': summarized_text
    })