from django.contrib import admin
from .models import category, recipe, recipeComment, ingredient

# Register your models here.
admin.site.register(category)
admin.site.register(recipe)
admin.site.register(recipeComment)
admin.site.register(ingredient)