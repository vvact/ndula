from django.contrib import admin
from .models import Sneaker, SneakerImage

class SneakerImageInline(admin.TabularInline):
    model = SneakerImage
    extra = 1  # show at least one blank image slot

class SneakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'available')
    inlines = [SneakerImageInline]
    search_fields = ('name', 'brand')
    list_filter = ('brand', 'available')

admin.site.register(Sneaker, SneakerAdmin)

