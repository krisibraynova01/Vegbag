from django.contrib import admin

from vegbag.blog.models import BlogPost


# Register your models here.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at']
    search_fields = ['title', 'author']
    list_filter = ['author', 'created_at', 'title']
    readonly_fields = ['created_at']
    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'image', 'author', 'short_description')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)  # Collapsible section for date information
        }),
    )
    date_hierarchy = 'created_at'  # Adding date hierarchy for easy date-based navigation
    list_per_page = 20  # Setting the number of items displayed per page in the admin list view

