from django.db.models import Q

from django.shortcuts import get_object_or_404, redirect, render
from .models import Recipe, Comment, Category
from .forms import CommentForm

def recipe_search(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = Recipe.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    
    return render(request, 'recipes/search_results.html', {
        'query': query,
        'results': results
    })

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

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    form = CommentForm()  
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe, 'form': form})

def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
    return redirect('recipe_detail', pk=recipe.id)

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=comment.recipe.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'recipes/edit_comment.html', {'form': form, 'comment': comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    recipe_id = comment.recipe.id
    if request.method == 'POST':
        comment.delete()
        return redirect('recipe_detail', pk=recipe_id)
    return render(request, 'recipes/delete_comment.html', {'comment': comment})
