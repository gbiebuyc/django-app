from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import ClientCompany, SupplierCompany, Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    filter_horizontal = ('company',)
    verbose_name_plural = 'Profile'

class MyUserAdmin(UserAdmin):
    list_filter = ('profile__company',) + UserAdmin.list_filter
    list_display = ('username', 'get_user_company', 'is_staff')
    readonly_fields = ('username',)
    fields = ('username',)
    inlines = [ ProfileInline, ]
    fieldsets = None
    def has_add_permission(self, request):
        return False
    def get_user_company(self, obj):
        return ', '.join(c.name for c in obj.profile.company.all())
    get_user_company.short_description = "User company"

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(ClientCompany)
admin.site.register(SupplierCompany)