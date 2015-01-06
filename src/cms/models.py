# Django Modules
from django.db import models

# App Modules
from accounts.models import User


class Category(models.Model):
    name = models.CharField(max_length=140, blank=False, null=False)
    slug = models.SlugField(max_length=140, unique=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created']


class Tag(models.Model):
    name = models.CharField(max_length=140, blank=False, null=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['-created']


class ArticleQuerySet(models.QuerySet):

    def published(self):
        return self.filter(publish=True)


class Article(models.Model):
    title = models.CharField(max_length=140, blank=False, null=False)
    slug = models.SlugField(max_length=140, unique=True)
    content = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    published_by = models.ForeignKey(User, blank=False, null=False)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=True, auto_now=True)

    objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
        ordering = ['-created']
