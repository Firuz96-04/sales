from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.


@admin.register(CustomUser)
class AdminUser(UserAdmin):
    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ('email', 'first_name', 'is_active',)
    list_display_links = ('first_name',)
    fieldsets = (
        # 'Additional Field',
        # {
        #     'fields': (
        #         'role',
        #     )
        # },
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    "role",
                    "status"
                ),
            },

        ),

        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


    # fieldsets = (
    #     *UserAdmin.fieldsets,
    #     (
    #         'Additional Field',
    #         {
    #             'fields': (
    #                 'role',
    #             )
    #         }
    #     )
    # )
    # add_fieldsets = (
    #     (None, {
    #         "classes": ("user",),
    #         "fields": (
    #             "email", "password1", "password2", "is_staff",
    #             "is_active", "groups", "user_permissions"
    #         )}
    #     )
    # )