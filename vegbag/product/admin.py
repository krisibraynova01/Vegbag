from django.contrib import admin
from vegbag.product.models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'price', 'is_discount']  # Customizing list display
    list_filter = ['category']
    search_fields = ['category', 'name']
    ordering = ['id']
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'price', 'is_discount', 'discount')
        }),
    )
 # Adding date hierarchy for easy date-based navigation
    list_per_page = 20
