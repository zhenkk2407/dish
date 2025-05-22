
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    cook_time = models.IntegerField(help_text="Время приготовления в минутах", verbose_name='Время готовки')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to="recipe_images/", verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, verbose_name='Ингредиент')
    amount = models.CharField(max_length=100, verbose_name='Количество')

    class Meta:
        verbose_name = 'Ингредиент рецепта'
        verbose_name_plural = 'Ингредиенты рецептов'

class InstructionStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    step_text = models.TextField(verbose_name='Текст шага')
    step_number = models.PositiveIntegerField(verbose_name='Номер шага')

    class Meta:
        verbose_name = 'Шаг инструкции'
        verbose_name_plural = 'Шаги инструкций'

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name='Рецепт')
    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название')
    recipes = models.ManyToManyField(Recipe, verbose_name='Рецепты')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'