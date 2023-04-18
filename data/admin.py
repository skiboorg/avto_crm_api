from django.contrib import admin
from .models import *


class WorkTypeInline (admin.TabularInline):
    model = WorkType
    extra = 0


class WorkCategoryAdmin(admin.ModelAdmin):
    model = WorkCategory
    inlines = [WorkTypeInline]

admin.site.register(WorkCategory,WorkCategoryAdmin)
admin.site.register(Client)