# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True, max_length=140)),
                ('content', models.TextField()),
                ('publish', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Article',
                'ordering': ['-created'],
                'verbose_name_plural': 'Articles',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('slug', models.SlugField(unique=True, max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Category',
                'ordering': ['-created'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Tag',
                'ordering': ['-created'],
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, blank=True, to='cms.Category'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='published_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='cms.Tag', null=True, blank=True),
            preserve_default=True,
        ),
    ]
