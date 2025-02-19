from django.contrib import admin
from .models import marvelModel
# Register your models here.

@admin.register(marvelModel)
class MarvelAdmin(admin.ModelAdmin):
    list_display =['id','name','heroic_name']

    
