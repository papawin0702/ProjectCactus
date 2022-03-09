from django.contrib import admin
from account.models import UserProfile
from django.contrib.auth.hashers import make_password, check_password

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["username","first_name","last_name","address","is_active"]
    list_filter = ["is_active","is_superuser","is_staff"]

    def save_model(self, request, obj, form, change):
        try:
            user_database = UserProfile.objects.get(pk=obj.pk)
        except Exception:
            user_database = None

        if user_database is None \
            or not(check_password(form.data["password"].user_database.password)
                   or user_database.password == form.data['password']):
            obj.password = make_password(obj.password)
        else:
            obj.password = user_database.password

        super().save_model(request, obj, form, change)


admin.site.register(UserProfile,UserProfileAdmin)
