# Django Modules
from django.shortcuts import render


def index(request):
    """Index view"""
    context = {}
    return render(request, 'cms/index.html', context)
