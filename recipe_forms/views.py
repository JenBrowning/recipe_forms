
# -*- coding: utf-8 -*-

from django.shortcuts import render
from recipe_forms.models import Recipes, Author
from django.contrib.auth.models import User
from recipe_forms.forms import AuthorsForm, RecipesForm

def index(request):
    html = 'index.html'
    stuff = Recipes.objects.all().order_by('title')
    return render(request, html, {'recipes': stuff})

def recipe_stuff(request, recipe_id):
    html = 'recipe.html'
    stuff = Recipes.objects.all().filter(id=recipe_id)
    return render(request, html, {'recipes': stuff})

def author_stuff(request, author_id):
    html = "author.html"
    stuff = Recipes.objects.all().filter(id=author_id)
    author = Author.objects.all().filter(id=author_id)
    return render(request, html, {'author': author, 'recipes': stuff})

def add_recipe(request):
    html = 'add_recipe.html'
    form = None

def add_author(request):
    html = 'add_author.html'
    form = None