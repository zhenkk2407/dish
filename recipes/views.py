from django.shortcuts import render, get_object_or_404
from .models import Recipe, Category


def index(request):
    recipes = Recipe.objects.all().order_by('-created_at')
    recipe_count = recipes.count()
    categories = Category.objects.all()
    random_recipe = Recipe.objects.order_by('?').first()
    latest_recipe = Recipe.objects.latest('created_at')
    
    context = {
        'recipes': recipes,
        'recipe_count': recipe_count,
        'categories': categories,
        'random_recipe': random_recipe,
        'latest_recipe': latest_recipe,
    }
    return render(request, 'recipes/index.html', context)

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    recipes = Recipe.objects.filter(category=category).order_by('-created_at')
    return render(request, 'recipes/category_detail.html', {'category': category, 'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


