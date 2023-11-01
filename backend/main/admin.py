from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from . import models

# Register your models here.


@admin.register(models.Category)
class CategoryAdmin(DraggableMPTTAdmin):
    sortable = 'name'
    mptt_indent_field = "name"
    search_fields = ("name",)    
    list_display = ("id",'tree_actions', 'indented_title', "name", "parent", "created_at", "is_active")
    list_editable = ("is_active", )
    list_display_links = ( "name", "indented_title")

    list_filter = ("name", "is_active")
    

@admin.register(models.BotUsers)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "username", "created_at", "is_active")
    search_fields = ("first_name", "last_name", "username")
    list_filter = ("created_at",)


@admin.register(models.Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("created_at", "user")


@admin.register(models.CourseSource)
class CourseSourceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "source", "created_at", "is_active")
    list_editable = ("is_active", )
    list_filter = ("created_at", "is_active", "category")
    search_fields = ("name", "category__name")