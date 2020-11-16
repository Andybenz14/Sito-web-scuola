from django.contrib import admin
from .models import Document

# Register your models here.

class DocAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Document, DocAdmin)
