from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('search/', views.recipe_search, name='recipe_search'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/comment/add/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]

