from django.contrib import admin

# Register your models here.
# blog.admin.py

from django.db import models

from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group
from django.utils.safestring import mark_safe

from blog.models import Category, Post
from django_summernote.admin import SummernoteModelAdmin

admin.site.unregister(Group)


@admin.register(Category)
class CategoryAdmin(SummernoteModelAdmin):
    model = Category
    list_per_page = 10
    date_hierarchy = "created_at"
    fieldsets = (
        ('Category', {
            'fields': ("name", "image",)
            }
        ),
    )
    list_display = (
        "category_name",
        "post_count",
    )
    list_display_links = [
        'category_name',
    ]
    list_filter = (
        "name",
        "created_at",
    )
    search_fields = (
        "name",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _post_count=models.Count("post", distinct=True)
        )
        return queryset
    
    def post_count(self, instance):
        return instance._post_count


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    model = Post
    list_per_page = 10
    date_hierarchy = "created_at"
    fieldsets = (
        (
            'Article', {
                'fields': (
                    "category",
                    "name",
                    "subtitle",
                    'body',
                    'image',
                    'status',
                    'published',
                )
            }
        ),
    )
    list_display = [
        "category",
        "name",
        "view",
        "status",
        "show_post_url",
        'published',
    ]
    list_display_links = [
        'name',
        'category'
    ]
    list_filter = (
        "status",
        "published",
    )
    list_editable = (
        "published",
        "status",
    )
    search_fields = (
        "name",
        "status",
    )
    
    @mark_safe
    @admin.display(description="Voir l'article")
    def show_post_url(self, instance):
        url = instance.get_absolute_url()
        response = format_html(f"""<a target="_blank" href="{url}">{url}</a>""")
        return response
