from django.contrib import admin
from store.models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ["name","created_at"]
    search_fields = ["name",]


admin.site.register(Store,StoreAdmin)
