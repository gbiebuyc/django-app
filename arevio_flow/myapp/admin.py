from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from . import models

class CompanyInline(admin.StackedInline):
    model = models.Company.users.through
    extra = 1

class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_superuser',),}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2'),}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_superuser',),}),
    )
    inlines = (CompanyInline,)
    list_filter = ('company', 'is_superuser',)
    list_display = ('get_full_name', 'get_user_company', 'is_superuser')
    def get_full_name(self, obj):
        return f'{obj.first_name} {obj.last_name}'
    get_full_name.short_description = "Full name"
    def get_user_company(self, obj):
        return ', '.join(c.name for c in obj.company_set.all())
    get_user_company.short_description = "User company(ies)"

class CompanyAdmin(admin.ModelAdmin):
    model = models.Company
    filter_horizontal = ('users',)

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, MyUserAdmin)
admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Taxonomy)
