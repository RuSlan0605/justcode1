from django.contrib import admin
from .models import Shop
from .models import Rubric

class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', )

admin.site.register(Shop, ShopAdmin)

class RubricAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(Rubric, RubricAdmin)