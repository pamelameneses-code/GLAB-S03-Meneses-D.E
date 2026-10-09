from django.shortcuts import render, get_object_or_404
from .models import Article, Category

def article_list(request):
    articles = Article.objects.filter(is_published=True).order_by('-published_at')
    categories = Category.objects.all()
    return render(request, 'news/article_list.html', {'articles': articles, 'categories': categories})

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, is_published=True)
    return render(request, 'news/article_detail.html', {'article': article})

def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = Article.objects.filter(category=category, is_published=True).order_by('-published_at')
    categories = Category.objects.all()
    return render(request, 'news/category_articles.html', {'category': category, 'articles': articles, 'categories': categories})