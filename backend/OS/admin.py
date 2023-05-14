from django.contrib import admin
from .models import OS



@admin.register(OS)
class OSAdmin(admin.ModelAdmin):
    list_display = ('name','description','create_at')