from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from users_api.models import YamdbUser


class YamdbUserInline(admin.StackedInline):
    model = YamdbUser
    can_delete = False
    verbose_name_plural = 'YamdbUsers'


class YamdbUserAdmin(BaseUserAdmin):
    inlines = (YamdbUserInline,)


admin.site.unregister(User)
admin.site.register(User, YamdbUserAdmin)
