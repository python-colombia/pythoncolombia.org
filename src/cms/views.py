# Django Modules
from django.shortcuts import render

# App Modules
from .models import Article


def index(request):
    """Index view"""
    context = {}
    context['articles'] = Article.objects.all().order_by('-created')
    return render(request, 'cms/index.html', context)


def article(request, slug):
    context = {}
    context['article'] = Article.objects.filter(slug=slug)
    return render(request, 'cms/article.html', context)


def articles(request, year=None, month=None, tag=None, author=None):
    if year:
        articles = Article.objects.filter(created__year=year)

    if month:
        articles = Article.objects.filter(created__month=month)

    if tag:
        articles = Article.objects.filter(tags__slug=tag)

    if author:
        articles = Article.objects.filter(author__username=author)

    context = {}
    context['articles'] = articles
    return render(request, 'cms/articles.html', context)
