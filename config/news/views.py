from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages


#Creating article

def create_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('create_article')  # Redirect to the home page after saving
        else:
            form = ArticleForm()
        return render(request, 'create_article.html', {'form': form})
    else:
        return redirect('login')

#Deleting article

def delete_article(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            article_id = request.POST.get('article_id')  # Get the article ID from the form
            article = get_object_or_404(Article, id=article_id)
            article.delete()
            return redirect('delete_article')  # Refresh the page after deletion

        articles = Article.objects.all().order_by('-published_date')
        return render(request, 'delete_article.html', {'articles': articles})
    else:
        return redirect('login')





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


# Login and Signup in viws

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'admin_base.html') # render to admin base page after login 
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

# Signup View
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                login(request, user)
                return redirect('home')  # Redirect to the home page after signup
        else:
            messages.error(request, 'Passwords do not match')
    
    return render(request, 'signup.html')

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')