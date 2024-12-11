from django.shortcuts import render, get_object_or_404
from .models import Article

def home(request):
    articles = Article.objects.all().order_by('-published_date')
    return render(request, 'post.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'article_detail.html', {'article': article})

def category(request, category_name):
    articles = Article.objects.filter(category__iexact=category_name)
    return render(request, 'post.html', {'articles': articles})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def our_team(request):
    return render(request, 'our_team.html')