from django.shortcuts import render, get_object_or_404
from .models import Article
from transformers import pipeline
from django.conf import settings

# Load the Hugging Face summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", tokenizer="facebook/bart-large-cnn")

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    # Summarize the article using Hugging Face API
    summary = summarizer(article.content, max_length=150, min_length=50, do_sample=False)
    summarized_text = summary[0]['summary_text']
    
    return render(request, 'news/article_detail.html', {'article': article, 'summary': summarized_text})
