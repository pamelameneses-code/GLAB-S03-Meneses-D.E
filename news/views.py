from django.shortcuts import get_object_or_404, render

from .models import Article, Category


def article_list(request):
    articles = (
        Article.objects.filter(is_published=True)
        .select_related("author", "category")
        .order_by("-published_at")
    )
    return render(request, "news/article_list.html", {
        "articles": articles,
        "categories": Category.objects.order_by("name"),
    })


def article_detail(request, slug):
    article = get_object_or_404(
        Article.objects.select_related("author", "category"),
        slug=slug,
        is_published=True,
    )
    return render(request, "news/article_detail.html", {
        "article": article,
        "categories": Category.objects.order_by("name"),
    })


def category_articles(request, slug):
    category = get_object_or_404(Category, slug=slug)
    articles = (
        category.articles.filter(is_published=True)
        .select_related("author", "category")
        .order_by("-published_at")
    )
    return render(request, "news/category_articles.html", {
        "category": category,
        "articles": articles,
        "categories": Category.objects.order_by("name"),
    })
