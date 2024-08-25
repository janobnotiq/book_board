from django.contrib import admin
from .models import Book,Category,Publisher

# Register your models here.

class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name",]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","slug"]
    prepopulated_fields = {"slug":("name",)}

class BookAdmin(admin.ModelAdmin):
    list_display = ["title","author"]

admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Publisher,PublisherAdmin)