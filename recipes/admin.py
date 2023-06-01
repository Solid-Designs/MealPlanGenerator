from django.contrib import admin
from .models import Ingredient, Recipe
# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_ingredients')

    def display_ingredients(self, obj):
        # Retrieve the related ingredients and format them
        ingredients = ', '.join(
            [ingredient.name for ingredient in obj.ingredient.all()])
        return ingredients


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
