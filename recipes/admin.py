
from django.contrib import admin
from .models import Category, Recipe, Ingredient, RecipeIngredient, InstructionStep, Comment, Tag


class RecipeForeignKeyAdminMixin:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'recipe':
            kwargs["queryset"] = Recipe.objects.all().order_by('id')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin, RecipeForeignKeyAdminMixin):
    list_display = ('id', 'recipe', 'ingredient', 'amount')
    list_select_related = ('recipe', 'ingredient')
    raw_id_fields = ('recipe', 'ingredient')

@admin.register(InstructionStep)
class InstructionStepAdmin(admin.ModelAdmin, RecipeForeignKeyAdminMixin):
    list_display = ('id', 'recipe', 'step_number', 'short_step_text')
    raw_id_fields = ('recipe',)
    
    def short_step_text(self, obj):
        return obj.step_text[:50] + '...' if len(obj.step_text) > 50 else obj.step_text
    short_step_text.short_description = 'Step Text'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin, RecipeForeignKeyAdminMixin):
    list_display = ('id', 'recipe', 'author_name', 'short_text', 'created_at')
    raw_id_fields = ('recipe',)

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Text'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    filter_horizontal = ('recipes',)  

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['name'] 

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(Category)


