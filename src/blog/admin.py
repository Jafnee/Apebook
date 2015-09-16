from django.contrib import admin

from .models import Post, Fruit, FruitEaten

class FruitEatenInline(admin.TabularInline):
    model = FruitEaten
    verbose_name = "Fruit eaten"
    verbose_name_plural = "Fruit eaten"
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('pub_date', 'text', 'total_calories', 'meal_size')
    inlines = [FruitEatenInline]

class FruitAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')

admin.site.register(Post, PostAdmin)
admin.site.register(Fruit, FruitAdmin)
