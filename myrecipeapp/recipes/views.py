from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    return render(request, 'recipe_list.html', context)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


@csrf_exempt
def recipe_create(request):
    form = RecipeForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    return render(request, 'recipe_form.html', {'form': form})


@csrf_exempt
def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None,
                      request.FILES or None, instance=recipe)
    if request.method == 'POST':
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    return render(request, 'recipe_form.html', {'form': form})


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('recipe_list')


def recipe_list_ajax(request):
    recipes = Recipe.objects.all()
    recipe_data = [{'title': recipe.title,
                    'description': recipe.description} for recipe in recipes]
    return JsonResponse({'recipes': recipe_data})
