from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from network.models import Link, Product


@admin.action(description="Очистить задолженность")
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0.00)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "id", "name", "country", "city", "product",  "supplier_link", "supplier_level", "debt", "created_at",
    )
    list_filter = ("city",)
    search_fields = ("name",)
    actions = [clear_debt]
    list_display_links = ("name",)

    def supplier_link(self, obj):
        link = reverse("admin:network_link_change", args=[obj.supplier_id])
        return format_html('<a href="{}">{}</a>', link, obj.supplier)

    supplier_link.short_description = "Поставщик"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "product_model", "release_date")
    search_fields = ("name",)
