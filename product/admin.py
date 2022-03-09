from django.contrib import admin
from product.models import Category,SubCategory,Product
# Register your models here.


class SubCateryInline(admin.TabularInline):
    model = SubCategory
    fk_name = "category"

class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCateryInline,]
    list_display = ("name","created_at","updated_at")

class SubCategoryAdmin(admin.ModelAdmin):
    search_fields = ["name","category__name"]
    list_display = ("name","fullname","created_at","updated_at")
    list_filter = ["category"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name","created_at"]
    search_fields = ["name","category__name","category__category__name"]
    filter_horizontal = ("category",)
    list_filter = ["category__category","category__name"]

admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Product,ProductAdmin)