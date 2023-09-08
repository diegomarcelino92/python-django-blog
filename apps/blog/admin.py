from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from apps.blog.models import Category, Page, Post, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    search_fields = 'id', 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {"slug": ('name',), }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug'
    list_display_links = 'id',
    search_fields = 'id', 'name', 'slug'
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = {"slug": ('name',), }


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published'
    list_display_links = 'id',
    search_fields = 'id', 'title', 'slug', 'content'
    list_filter = 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    list_per_page = 50
    prepopulated_fields = {"slug": ('title',), }


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = 'content',
    list_display = 'id', 'title', 'is_published', 'created_by'
    list_display_links = 'id',
    search_fields = 'id', 'title', 'slug', 'content', 'excertp', 'content',
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by',
    ordering = '-id',
    list_per_page = 50
    prepopulated_fields = {"slug": ('title',), }

    def save_model(self, req, model, _, change):
        if change:
            model.updated_by = req.user
        else:
            model.created_by = req.user

        model.save()
