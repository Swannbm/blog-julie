from django.contrib import admin

from .models import BlogPost, Photo


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ("title", "tags", "is_published")
    search_fields = ("tags", "title", "content")
    readonly_fields = ("slug", "created_date", "updated_date")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    model = BlogPost
    list_display = ("title", "tags")
    search_fields = ("title", "tags")
    readonly_fields = ("height", "width", "image_tag", "image_url")
    fields = ("title", "tags", "photo_file", "image_url", "image_tag")
