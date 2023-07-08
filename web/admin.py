from django.contrib import admin
from .models import Core
# Register your models here.


@admin.register(Core)
class CoreAdmin(admin.ModelAdmin):
    list_display = ("title",)
    prepopulated_fields = {"slug": ("title",)}