from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from .models import Company

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'Profile'

class CompanyInline(admin.StackedInline):
    model = Company.users.through
    extra = 1

class MyUserAdmin(UserAdmin):
    inlines = (CompanyInline,)
    list_filter = ('company',) + UserAdmin.list_filter
    list_display = ('username', 'get_user_company', 'is_staff')
    fields = ('username',)
    fieldsets = None
    def get_user_company(self, obj):
        return ', '.join(c.name for c in obj.company_set.all())
    get_user_company.short_description = "User company(ies)"

class CompanyAdmin(admin.ModelAdmin):
    model = Company
    filter_horizontal = ('users',)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(Company, CompanyAdmin)
